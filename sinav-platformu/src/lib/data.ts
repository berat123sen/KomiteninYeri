import type { ExamFile, ExamIndex } from "../types";

const BASE = import.meta.env.BASE_URL;

const indexCache = { value: null as ExamIndex | null };
const examCache = new Map<string, ExamFile>();

async function fetchJson<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE}${path}`);
  if (!res.ok) {
    throw new Error(`Veri yüklenemedi (${res.status}): ${path}`);
  }
  return (await res.json()) as T;
}

export async function loadIndex(): Promise<ExamIndex> {
  if (indexCache.value) return indexCache.value;
  const data = await fetchJson<ExamIndex>("data/index.json");
  indexCache.value = data;
  return data;
}

export async function loadExam(examId: string): Promise<ExamFile> {
  const cached = examCache.get(examId);
  if (cached) return cached;
  const data = await fetchJson<ExamFile>(`data/exams/${examId}.json`);
  examCache.set(examId, data);
  return data;
}

export function sourcePdfUrl(examId: string, page?: number): string {
  const base = `${BASE}kaynak/${examId}.pdf`;
  return page ? `${base}#page=${page}` : base;
}

export async function loadAllExams(): Promise<ExamFile[]> {
  const index = await loadIndex();
  return Promise.all(index.exams.map((e) => loadExam(e.id)));
}
