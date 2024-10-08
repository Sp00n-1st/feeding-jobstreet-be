from flask import jsonify, request
from src.controller import job_route
from src.services.job_service import create_job, del_job, edit_job, export_to_excel, get_all, scrape_job_data

@job_route.route('/generate', methods=['GET'])
def generate_data():
    return scrape_job_data(request.args.get('tag_id', 1))

@job_route.route('/jobs', methods=['POST'])
def insert_job():
    job_data = request.get_json()

    if not job_data:
        return jsonify({"error": "Invalid input"}), 400
    
    try:
        create_job(job_data)
        return jsonify({"message": "Job created successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@job_route.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    job_data = request.get_json()

    if not job_data or not job_id:
        return jsonify({"error": "Invalid input"}), 400
    
    try:
        edit_job(job_id, job_data)
        return jsonify({"message": "Job updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@job_route.route('/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    if not job_id:
        return jsonify({"error": "Invalid input"}), 400
    
    try:
        del_job(job_id)
        return jsonify({"message": "Job Delete successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@job_route.route('/job/export-excel', methods=['GET'])
def export_excel():
    try:
        return export_to_excel()
    except Exception as e:        
        return jsonify({"error": str(e)}), 500


@job_route.route('/jobs', methods=['GET'])
def fetch_all():
    tag = request.args.get('tag')
    try:
        return get_all(tag)
    except Exception as e:        
        return jsonify({"error": str(e)}), 500