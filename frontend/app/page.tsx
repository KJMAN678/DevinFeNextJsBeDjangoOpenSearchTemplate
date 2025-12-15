'use client'

import axios from 'axios';
import { useEffect, useState } from 'react';

export default function Page() {

  const [data, setData] = useState<{test: number }>({test: 0})

  useEffect(() => {
    axios.get(`${process.env.NEXT_PUBLIC_API_URL}/api/`)
    .then((res) => res.data)
    .then((data) => {
      setData(data)
    })
  }, [])

  // 検索フォームの入力結果をAPI経由でバックエンドに送信する
  async function onSubmit(e: React.FormEvent) {
  }

  return (
    <div>
      <h1>test</h1>
      <form onSubmit={onSubmit}>
        <input type="text" name="search_word" />
        <button type="submit">Search</button>
      </form>
      <p>{data.test}</p>
    </div>
  )
}
