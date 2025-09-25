export enum Status {
  OPEN = 'open',
  IN_PROGRESS = 'in_progress',
  CLOSED = 'closed'
}

export enum Priority {
  LOW = 'low',
  MEDIUM = 'medium',
  HIGH = 'high',
  URGENT = 'urgent'
}

export interface Issue {
  id: number;
  title: string;
  description?: string;
  status: Status;
  priority: Priority;
  assignee?: string;
  created_at: string;
  updated_at: string;
}

export interface IssueCreate {
  title: string;
  description?: string;
  status: Status;
  priority: Priority;
  assignee?: string;
}

export interface IssueUpdate {
  title?: string;
  description?: string;
  status?: Status;
  priority?: Priority;
  assignee?: string;
}

export interface IssueFilters {
  search?: string;
  status?: Status;
  priority?: Priority;
  assignee?: string;
  sortBy?: string;
  sortOrder?: 'asc' | 'desc';
  page: number;
  pageSize: number;
}