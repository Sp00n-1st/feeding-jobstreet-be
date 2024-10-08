import unittest
from unittest.mock import patch
from src.services.job_service import get_all

class SelectAllTest(unittest.TestCase):

    @patch('src.services.job_service.select_all')
    def test_get_all_success(self, mock_select_all):
        mock_select_all.return_value = [
            (1, 'Company A', 'Location A', 'Job Title A', 'Full-time', '100000', '2023-10-01', 1, 'Tag A'),
        ]

        result = get_all(1)

        expect_result = [
            (1, 'Company A', 'Location A', 'Job Title A', 'Full-time', '100000', '2023-10-01', 1, 'Tag A'),
        ]

        self.assertEqual(result, expect_result)

    @patch('src.services.job_service.select_all')
    def test_get_all_failed(self, mock_select_all):
        mock_select_all.return_value = [
            (2, 'Company E', 'Location Z', 'Job Title L', 'Kontrak', '1000000', '2023-10-02', 2, 'Tag U'),
        ]

        result = get_all(1)

        expect_result = [
            (1, 'Company E', 'Location Z', 'Job Title L', 'Kontrak', '1000000', '2023-10-02', 2, 'Tag U'),
        ]

        self.assertNotEqual(result, expect_result)

if __name__ == '__main__':
    unittest.main()
