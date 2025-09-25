import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Issue, IssueCreate, IssueUpdate, IssueFilters } from '../models/issue';

@Injectable({
  providedIn: 'root'
})
export class IssueService {
  private apiUrl = 'http://localhost:8000/api/v1';

  constructor(private http: HttpClient) { }

  getHealth(): Observable<any> {
    return this.http.get(`${this.apiUrl}/health`);
  }

  getIssues(filters: IssueFilters): Observable<Issue[]> {
    let params = new HttpParams()
      .set('page', filters.page.toString())
      .set('pageSize', filters.pageSize.toString());

    if (filters.search) params = params.set('search', filters.search);
    if (filters.status) params = params.set('status', filters.status);
    if (filters.priority) params = params.set('priority', filters.priority);
    if (filters.assignee) params = params.set('assignee', filters.assignee);
    if (filters.sortBy) params = params.set('sort_by', filters.sortBy);
    if (filters.sortOrder) params = params.set('sort_order', filters.sortOrder);

    return this.http.get<Issue[]>(`${this.apiUrl}/issues`, { params });
  }

  getIssue(id: number): Observable<Issue> {
    return this.http.get<Issue>(`${this.apiUrl}/issues/${id}`);
  }

  createIssue(issue: IssueCreate): Observable<Issue> {
    return this.http.post<Issue>(`${this.apiUrl}/issues`, issue);
  }

  updateIssue(id: number, issue: IssueUpdate): Observable<Issue> {
    return this.http.put<Issue>(`${this.apiUrl}/issues/${id}`, issue);
  }

  deleteIssue(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/issues/${id}`);
  }
}