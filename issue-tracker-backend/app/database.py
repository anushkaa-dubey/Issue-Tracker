from typing import Dict, List
from datetime import datetime
from .models import Issue, IssueCreate, IssueUpdate, Status, Priority

class Database:
    def __init__(self):
        self.issues: Dict[int, Issue] = {}
        self.next_id = 1
        self._initialize_sample_data()

    def _initialize_sample_data(self):
        sample_issues = [
            IssueCreate(
                title="Fix login bug",
                description="Users cannot login with correct credentials",
                status=Status.OPEN,
                priority=Priority.HIGH,
                assignee="john@example.com"
            ),
            IssueCreate(
                title="Add dark mode",
                description="Implement dark theme for the application",
                status=Status.IN_PROGRESS,
                priority=Priority.MEDIUM,
                assignee="sarah@example.com"
            ),
            IssueCreate(
                title="Update documentation",
                description="Update API documentation with new endpoints",
                status=Status.CLOSED,
                priority=Priority.LOW,
                assignee="mike@example.com"
            )
        ]
        
        for issue_data in sample_issues:
            self.create_issue(issue_data)

    def create_issue(self, issue: IssueCreate) -> Issue:
        now = datetime.now()
        new_issue = Issue(
            id=self.next_id,
            created_at=now,
            updated_at=now,
            **issue.dict()
        )
        self.issues[self.next_id] = new_issue
        self.next_id += 1
        return new_issue

    def get_issue(self, issue_id: int):
        return self.issues.get(issue_id)

    def get_all_issues(self) -> List[Issue]:
        return list(self.issues.values())

    def update_issue(self, issue_id: int, issue_update: IssueUpdate):
        if issue_id not in self.issues:
            return None
        
        existing_issue = self.issues[issue_id]
        update_data = issue_update.dict(exclude_unset=True)
        
        for field, value in update_data.items():
            setattr(existing_issue, field, value)
        
        existing_issue.updated_at = datetime.now()
        return existing_issue

    def delete_issue(self, issue_id: int) -> bool:
        if issue_id in self.issues:
            del self.issues[issue_id]
            return True
        return False

# Global database instance
db = Database()