import { NextRequest, NextResponse } from "next/server";

const BACKEND =
  process.env.BACKEND_URL ||
  "https://legal-tax-rag-265232236006.asia-south1.run.app";

export const maxDuration = 60;

export async function GET(req: NextRequest) {
  const q = req.nextUrl.searchParams.get("query") || "";
  if (!q.trim()) {
    return NextResponse.json({ error: "Please enter a question." }, { status: 400 });
  }
  try {
    const r = await fetch(`${BACKEND}/ask?query=${encodeURIComponent(q)}`, {
      cache: "no-store",
    });
    const data = await r.json();
    return NextResponse.json(data);
  } catch {
    return NextResponse.json(
      { error: "Could not reach the server. It may be waking up, so try again in a minute." },
      { status: 502 }
    );
  }
}
