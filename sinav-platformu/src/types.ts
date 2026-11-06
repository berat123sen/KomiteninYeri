export type AnswerStatus = "official" | "derived" | "missing";
export type ReviewStatus = "auto" | "approved" | "needs_review";
export type AnswerKey = "A" | "B" | "C" | "D" | "E";
export type QuestionType = "multiple_choice" | "true_false";

export interface Discipline {
  id: string;
  name: string;
  questionCount: number;
  first: number;
  last: number;
}

export interface Exam {
  id: string;
  label: string;
  shortLabel: string;
  year: string;
  period: number;
  term: string;
  questionCount: number;
  date?: string;
  sourceFile: string;
  sourcePages: number[];
  answerStatus: AnswerStatus;
  ocrQuality: "embedded" | "good" | "medium" | "poor";
  notes?: string;
  disciplines: Discipline[];
}

export interface Question {
  id: string;
  examId: string;
  number: number;
  disciplineId: string;
  discipline: string;
  type: QuestionType;
  stem: string;
  options: string[];
  correctAnswer: AnswerKey;
  sourcePage: number;
  answerStatus: AnswerStatus;
  confidence: number;
  reviewStatus: ReviewStatus;
  note?: string;
  explanation?: string;
}

export interface ExamFile {
  exam: Exam;
  questions: Question[];
}

export interface ExamSummary {
  id: string;
  label: string;
  shortLabel: string;
  year: string;
  period: number;
  term: string;
  questionCount: number;
  answerStatus: AnswerStatus;
  disciplines: Discipline[];
}

export interface ExamIndex {
  version: number;
  generatedAt: string;
  site: string;
  scope: string;
  exams: ExamSummary[];
}

export interface AnswerRecord {
  questionId: string;
  examId: string;
  disciplineId: string;
  selected: AnswerKey;
  correct: boolean;
  answeredAt: number;
}
