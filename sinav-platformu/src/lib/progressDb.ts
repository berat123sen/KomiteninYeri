import { openDB, type DBSchema, type IDBPDatabase } from "idb";
import type { AnswerRecord } from "../types";

interface ProgressDB extends DBSchema {
  answers: {
    key: string;
    value: AnswerRecord;
    indexes: { "by-exam": string; "by-discipline": string };
  };
}

const DB_NAME = "sinav-platformu";
const DB_VERSION = 1;

let dbPromise: Promise<IDBPDatabase<ProgressDB>> | null = null;

function getDb() {
  if (!dbPromise) {
    dbPromise = openDB<ProgressDB>(DB_NAME, DB_VERSION, {
      upgrade(db) {
        const store = db.createObjectStore("answers", { keyPath: "questionId" });
        store.createIndex("by-exam", "examId");
        store.createIndex("by-discipline", "disciplineId");
      },
    });
  }
  return dbPromise;
}

export async function getAllAnswers(): Promise<AnswerRecord[]> {
  const db = await getDb();
  return db.getAll("answers");
}

export async function putAnswer(record: AnswerRecord): Promise<void> {
  const db = await getDb();
  await db.put("answers", record);
}

export async function clearAnswers(): Promise<void> {
  const db = await getDb();
  await db.clear("answers");
}

export async function clearAnswersByExam(examId: string): Promise<void> {
  const db = await getDb();
  const tx = db.transaction("answers", "readwrite");
  const index = tx.store.index("by-exam");
  let cursor = await index.openCursor(IDBKeyRange.only(examId));
  while (cursor) {
    await cursor.delete();
    cursor = await cursor.continue();
  }
  await tx.done;
}
