import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Issue, IssueCreate, IssueUpdate, Status, Priority } from '../../models/issue';

@Component({
  selector: 'app-issue-form',
  templateUrl: './issue-form.component.html',
  styleUrls: ['./issue-form.component.css']
})
export class IssueFormComponent implements OnInit {
  @Input() issue: Issue | null = null;
  @Output() closed = new EventEmitter<void>();

  form: FormGroup;
  statusOptions = Object.values(Status);
  priorityOptions = Object.values(Priority);

  constructor(
    private fb: FormBuilder
  ) {
    this.form = this.createForm();
  }

  ngOnInit() {
    if (this.issue) {
      this.form.patchValue(this.issue);
    }
  }

  createForm(): FormGroup {
    return this.fb.group({
      title: ['', Validators.required],
      description: [''],
      status: [Status.OPEN, Validators.required],
      priority: [Priority.MEDIUM, Validators.required],
      assignee: ['']
    });
  }

  onSubmit() {
    if (this.form.valid) {
      console.log('Form submitted:', this.form.value);
      this.close();
    }
  }

  close() {
    this.closed.emit();
  }
}