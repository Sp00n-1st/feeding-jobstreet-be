from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from src.utils.util import parse_date

@dataclass
class Job:
    job_id: Optional[int] = None
    tag_id: Optional[int] = None
    tag_name: Optional[str] = None
    company_name: Optional[str] = None
    job_location: Optional[str] = None
    title: Optional[str] = None
    classification: Optional[str] = None
    subclassification: Optional[str] = None
    salary: Optional[str] = None
    work_type: Optional[str] = None
    teaser: Optional[str] = None
    work_arrangements: Optional[str] = None
    other_info: Optional[str] = None
    date: Optional[str] = None
    is_from_generate: Optional[bool] = None

    @classmethod
    def from_dict(cls, job: dict, tag_id: Optional[int] = None, is_from_generate: Optional[bool] = None) -> 'Job':
        return cls(
            job_id=job.get('job_id'),
            tag_id=tag_id,
            company_name=job.get('companyName'),
            job_location=job.get('location'),
            title=job.get('title'),
            classification=job.get('classification')['description'] if isinstance(job.get('classification'), dict) else None,
            subclassification=job.get('subClassification')['description'] if isinstance(job.get('subClassification'), dict) else None,
            salary=job.get('salary'),
            work_type=job.get('workType'),
            teaser=job.get('teaser'),
            work_arrangements=job.get('workArrangements').get('displayText') if isinstance(job.get('workArrangements'), dict) else None,
            other_info=", ".join(job.get('bulletPoints', [])),
            date=parse_date(job.get('listingDate')),
            is_from_generate=is_from_generate
        )
