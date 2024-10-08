# import unittest
# import xlwt
# from unittest.mock import patch, MagicMock
# from io import BytesIO
# from flask import Response
# from src.services.job_service import export_to_excel

# class TestExportToExcel(unittest.TestCase):

#     @patch('src.utils.util.get_connection')
#     @patch('src.repository.job_repository.select_all')
#     def test_export_to_excel(self, mock_select_all, mock_get_connection):
#         # Arrange
#         mock_conn = MagicMock()
#         mock_get_connection.return_value = mock_conn

#         # Create mock data
#         mock_job_data = [
#             MagicMock(job_id=1, title='Job Title 1', company_name='Company 1', work_type='Full-time',
#                       job_location='Location 1', salary='1000', date='2023-10-08', tag_name='Tag 1'),
#             MagicMock(job_id=2, title='Job Title 2', company_name='Company 2', work_type='Part-time',
#                       job_location='Location 2', salary='2000', date='2023-10-09', tag_name='Tag 2'),
#         ]
#         mock_select_all.return_value = mock_job_data

#         # Act
#         response = export_to_excel()

#         # Assert
#         self.assertIsInstance(response, Response)
#         self.assertEqual(response.content_type, 'application/vnd.ms-excel')
#         self.assertIn('attachment; filename=jobs_export.xls', response.headers['Content-Disposition'])

#         # Check the content of the Excel file
#         output = BytesIO(response.data)
#         output.seek(0)  # Ensure we are at the start of the BytesIO stream
        
#         # Load the workbook from the BytesIO stream
#         workbook = xlwt.Workbook(encoding='utf-8')
#         worksheet = workbook.add_sheet('Jobs')

#         # Manually load the response data into the workbook for checking
#         workbook.save(output)  # Save the mock data into the workbook
        
#         # Now read the output from BytesIO and check the contents
#         output.seek(0)  # Seek back to the start after saving
#         workbook = xlwt.Workbook()
#         workbook.load_workbook(output)  # Load the workbook directly from the BytesIO stream
#         worksheet = workbook.get_sheet(0)

#         # Check headers
#         headers = ['ID', 'Title', 'Company Name', 'Work Type', 'Location', 'Salary', 'Listing Date', 'Tag']
#         for col_num, header in enumerate(headers):
#             self.assertEqual(worksheet.cell_value(0, col_num), header)

#         # Check job data
#         for row_num, job in enumerate(mock_job_data, start=1):
#             self.assertEqual(worksheet.cell_value(row_num, 0), str(job.job_id))
#             self.assertEqual(worksheet.cell_value(row_num, 1), job.title)
#             self.assertEqual(worksheet.cell_value(row_num, 2), job.company_name)
#             self.assertEqual(worksheet.cell_value(row_num, 3), job.work_type)
#             self.assertEqual(worksheet.cell_value(row_num, 4), job.job_location)
#             self.assertEqual(worksheet.cell_value(row_num, 5), job.salary)
#             self.assertEqual(worksheet.cell_value(row_num, 6), job.date)
#             self.assertEqual(worksheet.cell_value(row_num, 7), job.tag_name)

#     @patch('src.utils.util.get_connection')
#     @patch('src.repository.job_repository.select_all')
#     def test_export_to_excel_no_data(self, mock_select_all, mock_get_connection):
#         # Arrange
#         mock_get_connection.return_value = MagicMock()
#         mock_select_all.return_value = []  # No jobs

#         # Act
#         response = export_to_excel()

#         # Assert
#         self.assertIsInstance(response, Response)
#         self.assertEqual(response.content_type, 'application/vnd.ms-excel')
#         self.assertIn('attachment; filename=jobs_export.xls', response.headers['Content-Disposition'])

#         # Check the content of the Excel file
#         output = BytesIO(response.data)
#         output.seek(0)  # Ensure we are at the start of the BytesIO stream
        
#         # Load the workbook from the BytesIO stream
#         workbook = xlwt.Workbook(encoding='utf-8')
#         workbook.save(output)  # Save the empty output to the workbook
#         output.seek(0)  # Seek back to the start after saving

#         # Now, check that there is only the header row
#         workbook = xlwt.Workbook()
#         worksheet = workbook.add_sheet('Jobs')
#         self.assertEqual(worksheet.nrows, 1)  # Only the header row should exist

# if __name__ == '__main__':
#     unittest.main()
