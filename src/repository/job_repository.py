from typing import List
from psycopg2.extensions import connection
from src.model.job import Job


def insert_datas(jobs: List[Job], conn: connection):
    cursor = conn.cursor()
    cursor.executemany(
        """
            INSERT INTO jobs (
                tag_id, 
                company_name, 
                job_location, 
                title, 
                classification, 
                subclassification, 
                salary, 
                work_type, 
                teaser, 
                work_arrangements, 
                other_info, 
                date,
                is_from_generate
            ) VALUES (
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s, 
                %s,
                %s
            )
    """, [
            (
                job.tag_id,
                job.company_name,
                job.job_location,
                job.title,
                job.classification,
                job.subclassification,
                job.salary,
                job.work_type,
                job.teaser,
                job.work_arrangements,
                job.other_info,
                job.date,
                job.is_from_generate
            )
            for job in jobs
        ])
    cursor.close()

def insert_data(job: Job, conn: connection):
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO jobs (
                tag_id, 
                company_name, 
                job_location, 
                title, 
                classification, 
                subclassification, 
                salary, 
                work_type, 
                teaser, 
                work_arrangements, 
                other_info, 
                date,
                is_from_generate
            ) VALUES (
                %(tag_id)s,
                %(company_name)s,
                %(job_location)s,
                %(title)s,
                %(classification)s,
                %(subclassification)s,
                %(salary)s,
                %(work_type)s,
                %(teaser)s,
                %(work_arrangements)s,
                %(other_info)s,
                %(date)s,
                FALSE
            )""", job.__dict__)
    cursor.close()

def update_job(job_id, job, conn:connection):
    cursor = conn.cursor()
    cursor.execute(
        f"""
            UPDATE jobs
            SET 
                tag_id = %(tag_id)s,
                company_name = %(company_name)s,
                job_location = %(job_location)s,
                title = %(title)s,
                classification = %(classification)s,
                subclassification = %(subclassification)s,
                salary = %(salary)s,
                work_type = %(work_type)s,
                teaser = %(teaser)s,
                work_arrangements = %(work_arrangements)s,
                other_info = %(other_info)s,
                date = %(date)s
            WHERE job_id = {job_id}
        """, job)
    cursor.close()

def delete_by_tag_id(tag_id, conn:connection):
    cursor = conn.cursor()
    cursor.execute(
        f"""
            DELETE FROM jobs
            WHERE
                tag_id = {tag_id} AND
                is_from_generate = TRUE
        """
    )
    cursor.close()

def delete_by_id(job_id, conn:connection):
    cursor = conn.cursor()
    cursor.execute(
        f"""
            DELETE FROM jobs
            WHERE
                job_id = {job_id} 
        """
    )
    cursor.close()

def select_all(conn:connection, filter:str) -> List[Job]:
    cursor = conn.cursor()
    cursor.execute(
        f"""
            SELECT DISTINCT
                j.job_id,
                j.company_name,
                j.job_location,
                j.title,
                j.work_type,
                j.salary,
                j.date,
                t.tag_id,
                t.tag_name
            FROM jobs j 
            LEFT JOIN tag t ON t.tag_id = j.tag_id
            {filter}
            ORDER BY j.title ASC
        """
    )

    rows = cursor.fetchall()
    cursor.close()

    return [Job(job_id=row[0],                 
                company_name=row[1], 
                job_location=row[2], 
                title=row[3], 
                work_type=row[4], 
                salary=row[5], 
                date=row[6], 
                tag_id=row[7],
                tag_name=row[8]) for row in rows]