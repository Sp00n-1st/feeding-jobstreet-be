from io import BytesIO
import json
import xlwt
from bs4 import BeautifulSoup
from flask import Response, jsonify
import requests
from src.model.job import Job
from src.repository.job_repository import delete_by_id, delete_by_tag_id, insert_data, insert_datas, select_all, update_job
from src.repository.tag_repository import get_by_id
from src.utils.util import get_connection

def scrape_job_data(tag_id):
    try:
        conn = get_connection()  
        url = f'https://id.jobstreet.com/id/{get_by_id(conn, tag_id)}-jobs'
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        script_content = ""

        for script in soup.find_all('script'):
            if 'window.SEEK_REDUX_DATA' in script.string:
                script_content = script.string
                break

        start_index = script_content.find("window.SEEK_REDUX_DATA = ")
        if start_index != -1:
            json_string = script_content[start_index + len("window.SEEK_REDUX_DATA = "):]
            end_index = json_string.find("};") + 1
            json_string = json_string[:end_index]

            try:
                config = json.loads(json_string)
                jobs = config.get('results', {}).get('results', {}).get('jobs', [])
                if jobs:   
                    try:                        
                        delete_by_tag_id(tag_id,conn)
                        insert_datas(jobs=[Job.from_dict(job, tag_id=tag_id, is_from_generate=True) for job in jobs], conn=conn)
                        conn.commit()
                    except Exception as e:     
                        if conn:
                            conn.rollback()                   
                        print("Error Insert Data:", e)
                        return None
                    finally:
                        if conn:
                            conn.close()
                    return jsonify({
                        "message": "Successfully Generate Data"
                    })

                else:
                    return None 
            except json.JSONDecodeError as e:
                print("JSON Decode Error:", e)
                return None 
        else:
            print("SEEK_REDUX_DATA not found.")
            return None

    except requests.RequestException as req_err:
        print("Request Error:", req_err)
        return None

    
def create_job(job):
    conn = None
    try:
        conn = get_connection()
        insert_data(Job.from_dict(job, tag_id=job['tag_id']), conn)
        conn.commit()  
    except Exception as e:
        print("Error Insert Data:", e)
        if conn:
            conn.rollback()
        return None
    finally:
        if conn:
            conn.close()

def edit_job(job_id, job):
    try:
        conn = get_connection()
        update_job(job_id, job, conn)
        conn.commit()  
    except Exception as e:
        print("Error Update Data:", e)
        if conn:
            conn.rollback()
        return None
    finally:
        if conn:
            conn.close()

def del_job(job_id):
    try:
        conn = get_connection()
        delete_by_id(job_id, conn)
        conn.commit()  
    except Exception as e:
        print("Error Delete Data:", e)
        if conn:
            conn.rollback()
        return None
    finally:
        if conn:
            conn.close()

def export_to_excel():
    work_book = xlwt.Workbook()
    work_sheet = work_book.add_sheet('Jobs')

    headers = ['ID', 'Title', 'Company Name', 'Work Type', 'Location', 'Salary', 'Listing Date', 'Tag']
    for col_num, header in enumerate(headers):
        work_sheet.write(0, col_num, header)

    try:
        conn = get_connection()

        data = select_all(conn,'')
    finally:        
        conn.close()

    for row_num, job in enumerate(data, start=1):
        work_sheet.write(row_num, 0, str(job.job_id))
        work_sheet.write(row_num, 1, job.title)
        work_sheet.write(row_num, 2, job.company_name)
        work_sheet.write(row_num, 3, job.work_type)
        work_sheet.write(row_num, 4, job.job_location)
        work_sheet.write(row_num, 5, job.salary)
        work_sheet.write(row_num, 6, job.date)
        work_sheet.write(row_num, 7, job.tag_name)

    output = BytesIO()
    work_book.save(output)
    output.seek(0)

    response = Response(output.getvalue(), content_type='application/vnd.ms-excel')
    response.headers['Content-Disposition'] = 'attachment; filename=jobs_export.xls'
    return response

def get_all(tag_id):
    try:
        conn = get_connection()
        result = select_all(conn, f'WHERE j.tag_id = {tag_id}' if tag_id else '')
    finally:
        conn.close()
    return result 
    
