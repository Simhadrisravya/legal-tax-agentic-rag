"use client";

import { useState } from "react";

type Result = {
  question?: string;
  document?: string | null;
  section?: string | null;
  answer?: string;
  sources?: string[];
  error?: string;
};

const EXAMPLES = [
  "What is covered under Section 24 of the Income Tax Act?",
  "What does Section 16 of the GST Act say about input tax credit?",
  "Who is required to register under GST?",
];

export default function Home() {
  const [query, setQuery] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<Result | null>(null);

  async function ask(q: string) {
    if (!q.trim() || loading) return;
    setLoading(true);
    setResult(null);
    try {
      const r = await fetch(`/api/ask?query=${encodeURIComponent(q)}`);
      setResult(await r.json());
    } catch {
      setResult({ error: "Something went wrong. Please try again." });
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="mx-auto min-h-screen max-w-3xl px-4 py-10 text-zinc-900 dark:text-zinc-100">
      <h1 className="text-3xl font-bold">Legal &amp; Tax Assistant</h1>
      <p className="mt-2 text-zinc-600 dark:text-zinc-400">
        Ask about the Indian Income Tax Act and GST Act. Answers cite the source text.
      </p>

      <div className="mt-6 flex gap-2">
        <input
          className="flex-1 rounded-lg border border-zinc-300 bg-white px-4 py-3 text-zinc-900 dark:border-zinc-700 dark:bg-zinc-900 dark:text-zinc-100"
          placeholder="e.g. What is covered under Section 80C?"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          onKeyDown={(e) => e.key === "Enter" && ask(query)}
        />
        <button
          className="rounded-lg bg-blue-600 px-5 py-3 font-medium text-white disabled:opacity-50"
          onClick={() => ask(query)}
          disabled={loading || !query.trim()}
        >
          {loading ? "Thinking..." : "Ask"}
        </button>
      </div>

      <div className="mt-3 flex flex-wrap gap-2">
        {EXAMPLES.map((ex) => (
          <button
            key={ex}
            className="rounded-full border border-zinc-300 px-3 py-1 text-sm hover:bg-zinc-100 dark:border-zinc-700 dark:hover:bg-zinc-800"
            onClick={() => {
              setQuery(ex);
              ask(ex);
            }}
          >
            {ex}
          </button>
        ))}
      </div>

      {loading && (
        <p className="mt-6 text-zinc-500">
          Searching the law... the first question after a quiet period can take up to a minute.
        </p>
      )}

      {result && (
        <section className="mt-8 rounded-xl border border-zinc-200 p-5 dark:border-zinc-800">
          {result.error ? (
            <p className="text-red-600">{result.error}</p>
          ) : (
            <>
              {(result.document || result.section) && (
                <p className="mb-2 text-sm text-zinc-500">
                  {result.document}
                  {result.section ? ` - Section ${result.section}` : ""}
                </p>
              )}
              <p className="whitespace-pre-wrap leading-relaxed">{(result.answer || "").split("**").map((part, i) => i % 2 === 1 ? <strong key={i}>{part}</strong> : part)}</p>
              {result.sources && result.sources.length > 0 && (
                <details className="mt-4">
                  <summary className="cursor-pointer font-medium">
                    Sources ({result.sources.length})
                  </summary>
                  <div className="mt-2 space-y-3">
                    {result.sources.map((s, i) => (
                      <pre
                        key={i}
                        className="max-h-60 overflow-auto whitespace-pre-wrap rounded bg-zinc-100 p-3 text-xs dark:bg-zinc-900"
                      >
                        {s}
                      </pre>
                    ))}
                  </div>
                </details>
              )}
            </>
          )}
        </section>
      )}

      <p className="mt-10 text-xs text-zinc-500">
        For information only. This is not legal or tax advice. Please consult a qualified professional.
      </p>
    </main>
  );
}

