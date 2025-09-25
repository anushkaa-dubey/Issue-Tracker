from fastapi import APIRouter, HTTPException, Query
from typing import Optional, List
from ..database import db
from ..models import Issue, IssueCreate, IssueUpdate, Status, Priority

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.get("/issues", response_model=List[Issue])
async def get_issues(
    search: Optional[str] = Query(None, description="Search by title"),
    status: Optional[Status] = Query(None, description="Filter by status"),
    priority: Optional[Priority] = Query(None, description="Filter by priority"),
    assignee: Optional[str] = Query(None, description="Filter by assignee"),
    sort_by: Optional[str] = Query("updated_at", description="Sort by field"),
    sort_order: Optional[str] = Query("desc", description="Sort order (asc/desc)"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(10, ge=1, le=100, description="Items per page")
):
    issues = db.get_all_issues()
    
    # Apply search
    if search:
        issues = [issue for issue in issues if search.lower() in issue.title.lower()]
    
    # Apply filters
    if status:
        issues = [issue for issue in issues if issue.status == status]
    if priority:
        issues = [issue for issue in issues if issue.priority == priority]
    if assignee:
        issues = [issue for issue in issues if issue.assignee and assignee.lower() in issue.assignee.lower()]
    
    # Apply sorting
    reverse = sort_order.lower() == "desc"
    try:
        issues.sort(key=lambda x: getattr(x, sort_by), reverse=reverse)
    except AttributeError:
        # Fallback to updated_at if invalid sort field
        issues.sort(key=lambda x: x.updated_at, reverse=reverse)
    
    # Apply pagination
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    paginated_issues = issues[start_idx:end_idx]
    
    return paginated_issues

@router.get("/issues/{issue_id}", response_model=Issue)
async def get_issue(issue_id: int):
    issue = db.get_issue(issue_id)
    if issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return issue

@router.post("/issues", response_model=Issue)
async def create_issue(issue: IssueCreate):
    return db.create_issue(issue)

@router.put("/issues/{issue_id}", response_model=Issue)
async def update_issue(issue_id: int, issue_update: IssueUpdate):
    updated_issue = db.update_issue(issue_id, issue_update)
    if updated_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return updated_issue

@router.delete("/issues/{issue_id}")
async def delete_issue(issue_id: int):
    if not db.delete_issue(issue_id):
        raise HTTPException(status_code=404, detail="Issue not found")
    return {"message": "Issue deleted successfully"}