'use client'

import axios from 'axios';
import { useState } from 'react';

interface SearchResult {
  took: number;
  total: number;
  results: Array<{
    Name: string;
    Age: number;
    Sex: string;
  }>;
}

export default function Page() {
  const [data, setData] = useState<SearchResult | null>(null);
  const [loading, setLoading] = useState(false);

  // 検索フォームの入力結果をAPI経由でバックエンドに送信する
  async function onSubmit(e: React.FormEvent) {
    e.preventDefault()
    setLoading(true);
    const formData = new FormData(e.target as HTMLFormElement)
    const searchWord = (formData.get('search_word') as string | null)?.trim() ?? ''

    // 空文字列・空白のみの場合はAPIリクエストを行わない
    if (!searchWord) {
      setLoading(false);
      setData(null);
      return;
    }

    try {
      const res = await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/api/search`, { search_word: searchWord })
      setData(res.data)
    } catch (error: unknown) {
      console.error('APIエラー:', error)
      if (axios.isAxiosError(error)) {
        console.error('レスポンスデータ:', error.response?.data)
        console.error('ステータスコード:', error.response?.status)
        console.error('リクエストURL:', error.config?.url)
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <h1>検索</h1>
      <form onSubmit={onSubmit}>
        <input type="text" name="search_word" />
        <button type="submit" disabled={loading}>
          {loading ? '検索中...' : 'Search'}
        </button>
      </form>
      
      {data && (
        <div>
          <p>検索時間: {data.took}ms</p>
          <p>検索結果数: {data.total}</p>
          {data.results.length > 0 ? (
            <ul>
              {data.results.map((result, index) => (
                <li key={index}>
                  <strong>{result.Name}</strong> - 年齢: {result.Age}, 性別: {result.Sex}
                </li>
              ))}
            </ul>
          ) : (
            <p>検索結果がありません</p>
          )}
        </div>
      )}
    </div>
  )
}
