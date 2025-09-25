import { Component, OnInit } from '@angular/core';
import { Issue, IssueFilters, Status, Priority } from '../../models/issue';
import { IssueService } from '../../services/issue.service';

@Component({
  selector: 'app-issue-list',
  templateUrl: './issue-list.component.html',
  styleUrls: ['./issue-list.component.css']
})
export class IssueListComponent implements OnInit {
  issues: Issue[] = [];
  filters: IssueFilters = {
    page: 1,
    pageSize: 10
  };
  totalItems = 0;
  loading = false;

  statusOptions = Object.values(Status);
  priorityOptions = Object.values(Priority);

  showForm = false;
  selectedIssue: Issue | null = null;
  editingIssue: Issue | null = null;

  constructor(private issueService: IssueService) {}

  ngOnInit() {
    this.loadIssues();
  }

  loadIssues() {
    this.loading = true;
    this.issueService.getIssues(this.filters).subscribe({
      next: (issues) => {
        this.issues = issues;
        this.loading = false;
      },
      error: (error) => {
        console.error('Error loading issues:', error);
        this.loading = false;
      }
    });
  }

onSearchChange(event: any) {
  this.filters.search = event.target.value;
  this.filters.page = 1;
  this.loadIssues();
}
  onFilterChange() {
    this.filters.page = 1;
    this.loadIssues();
  }

  onPageChange(page: number) {
    this.filters.page = page;
    this.loadIssues();
  }

  onCreateIssue() {
    this.editingIssue = null;
    this.showForm = true;
  }

  onEditIssue(issue: Issue) {
    this.editingIssue = issue;
    this.showForm = true;
  }

  onIssueSelected(issue: Issue) {
    this.selectedIssue = issue;
  }

  onFormClosed() {
    this.showForm = false;
    this.editingIssue = null;
    this.loadIssues();
  }

  onDetailClosed() {
    this.selectedIssue = null;
  }
}