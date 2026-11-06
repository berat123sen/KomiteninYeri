import { create } from "zustand";
import type { AnswerKey, AnswerRecord, Question } from "../types";
import { clearAnswers, clearAnswersByExam, getAllAnswers, putAnswer } from "../lib/progressDb";

interface ProgressState {
  answers: Record<string, AnswerRecord>;
  loaded: boolean;
  init: () => Promise<void>;
  record: (question: Question, selected: AnswerKey) => Promise<AnswerRecord>;
  reset: () => Promise<void>;
  resetExam: (examId: string) => Promise<void>;
}

export const useProgressStore = create<ProgressState>()((set, get) => ({
  answers: {},
  loaded: false,
  init: async () => {
    if (get().loaded) return;
    try {
      const all = await getAllAnswers();
      const map: Record<string, AnswerRecord> = {};
      for (const a of all) map[a.questionId] = a;
      set({ answers: map, loaded: true });
    } catch (err) {
      console.error("İlerleme yüklenemedi", err);
      set({ loaded: true });
    }
  },
  record: async (question, selected) => {
    const record: AnswerRecord = {
      questionId: question.id,
      examId: question.examId,
      disciplineId: question.disciplineId,
      selected,
      correct: selected === question.correctAnswer,
      answeredAt: Date.now(),
    };
    set((state) => ({ answers: { ...state.answers, [question.id]: record } }));
    try {
      await putAnswer(record);
    } catch (err) {
      console.error("İlerleme kaydedilemedi", err);
    }
    return record;
  },
  reset: async () => {
    await clearAnswers();
    set({ answers: {} });
  },
  resetExam: async (examId) => {
    await clearAnswersByExam(examId);
    set((state) => {
      const next = { ...state.answers };
      for (const key of Object.keys(next)) {
        if (next[key].examId === examId) delete next[key];
      }
      return { answers: next };
    });
  },
}));
