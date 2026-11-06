import { useEffect } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Layout } from "./components/Layout";
import { Home } from "./pages/Home";
import { Browse } from "./pages/Browse";
import { ExamPage } from "./pages/Exam";
import { QuestionDetail } from "./pages/QuestionDetail";
import { TestPage } from "./pages/Test";
import { RandomPage } from "./pages/Random";
import { ProgressPage } from "./pages/Progress";
import { NotFound } from "./pages/NotFound";
import { useProgressStore } from "./store/useProgressStore";

export default function App() {
  const init = useProgressStore((s) => s.init);

  useEffect(() => {
    void init();
  }, [init]);

  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route index element={<Home />} />
          <Route path="cikmislar" element={<Browse />} />
          <Route path="sinav/:examId" element={<ExamPage />} />
          <Route path="sinav/:examId/soru/:number" element={<QuestionDetail />} />
          <Route path="test/:examId" element={<TestPage />} />
          <Route path="rastgele" element={<RandomPage />} />
          <Route path="ilerleme" element={<ProgressPage />} />
          <Route path="*" element={<NotFound />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
