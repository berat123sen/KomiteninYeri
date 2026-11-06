import { useEffect, useState } from "react";
import type { ExamFile, ExamIndex } from "../types";
import { loadAllExams, loadExam, loadIndex } from "./data";

export function useExamIndex() {
  const [index, setIndex] = useState<ExamIndex | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let alive = true;
    loadIndex()
      .then((data) => {
        if (alive) setIndex(data);
      })
      .catch((err: unknown) => {
        if (alive) setError(err instanceof Error ? err.message : "Veri yüklenemedi.");
      });
    return () => {
      alive = false;
    };
  }, []);

  return { index, error, loading: !index && !error };
}

export function useExam(examId: string | undefined) {
  const [data, setData] = useState<ExamFile | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!examId) return;
    let alive = true;
    setData(null);
    setError(null);
    loadExam(examId)
      .then((exam) => {
        if (alive) setData(exam);
      })
      .catch((err: unknown) => {
        if (alive) setError(err instanceof Error ? err.message : "Sınav yüklenemedi.");
      });
    return () => {
      alive = false;
    };
  }, [examId]);

  return { data, error, loading: !data && !error };
}

export function useAllExams() {
  const [data, setData] = useState<ExamFile[] | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let alive = true;
    loadAllExams()
      .then((exams) => {
        if (alive) setData(exams);
      })
      .catch((err: unknown) => {
        if (alive) setError(err instanceof Error ? err.message : "Sınavlar yüklenemedi.");
      });
    return () => {
      alive = false;
    };
  }, []);

  return { data, error, loading: !data && !error };
}
