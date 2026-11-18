import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { login } from '../api'

export default function LoginPage() {
  const [email, setEmail] = useState('admin@lawfirm.com')
  const [password, setPassword] = useState('Admin@123')
  const [error, setError] = useState('')
  const navigate = useNavigate()

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    try {
      const response = await login(email, password)
      localStorage.setItem('token', response.data.token)
      navigate('/')
    } catch (err) {
      setError('Invalid credentials or backend not running')
    }
  }

  return (
    <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-slate-900 to-blue-800 p-6">
      <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-xl">
        <h1 className="mb-1 text-3xl font-bold">LegalFlow</h1>
        <p className="mb-6 text-slate-500">Cloud-based law firm management</p>
        <form className="space-y-4" onSubmit={submit}>
          <div>
            <label className="label">Email</label>
            <input className="input" value={email} onChange={(e) => setEmail(e.target.value)} />
          </div>
          <div>
            <label className="label">Password</label>
            <input type="password" className="input" value={password} onChange={(e) => setPassword(e.target.value)} />
          </div>
          {error && <p className="text-sm text-red-500">{error}</p>}
          <button className="btn btn-primary w-full" type="submit">Login</button>
        </form>
      </div>
    </div>
  )
}
