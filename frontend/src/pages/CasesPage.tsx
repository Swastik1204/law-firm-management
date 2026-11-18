import { useEffect, useState } from 'react'
import { createCase, deleteCase, getCases, updateCase } from '../api'
import type { CaseItem } from '../types'

const empty: Omit<CaseItem, 'id' | 'clientName'> = {
  caseNumber: '', title: '', caseType: '', clientId: 0, lawyerIds: [], courtName: '', filingDate: '', nextHearingDate: '', description: '', status: 'ACTIVE'
}

export default function CasesPage() {
  const [cases, setCases] = useState<CaseItem[]>([])
  const [form, setForm] = useState(empty)
  const [editingId, setEditingId] = useState<number | null>(null)

  const load = async () => {
    const res = await getCases()
    setCases(res.data)
  }

  useEffect(() => { load() }, [])

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (editingId) await updateCase(editingId, form)
    else await createCase(form)
    setForm(empty)
    setEditingId(null)
    load()
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-3xl font-bold">Cases</h2>
        <button className="btn btn-primary" onClick={() => setForm(empty)}>New Case</button>
      </div>
      <div className="grid lg:grid-cols-3 gap-6">
        <form className="card lg:col-span-1 space-y-3" onSubmit={submit}>
          <h3 className="text-xl font-semibold">{editingId ? 'Edit Case' : 'Add Case'}</h3>
          <input className="input" placeholder="Case number" value={form.caseNumber} onChange={(e) => setForm({ ...form, caseNumber: e.target.value })} />
          <input className="input" placeholder="Title" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} />
          <input className="input" placeholder="Case type" value={form.caseType} onChange={(e) => setForm({ ...form, caseType: e.target.value })} />
          <input className="input" type="number" placeholder="Client ID" value={form.clientId} onChange={(e) => setForm({ ...form, clientId: Number(e.target.value) })} />
          <input className="input" placeholder="Court name" value={form.courtName} onChange={(e) => setForm({ ...form, courtName: e.target.value })} />
          <input className="input" type="date" value={form.filingDate} onChange={(e) => setForm({ ...form, filingDate: e.target.value })} />
          <input className="input" type="date" value={form.nextHearingDate || ''} onChange={(e) => setForm({ ...form, nextHearingDate: e.target.value })} />
          <textarea className="input" placeholder="Description" value={form.description} onChange={(e) => setForm({ ...form, description: e.target.value })} />
          <input className="input" placeholder="Status" value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value })} />
          <button className="btn btn-primary w-full">Save</button>
        </form>
        <div className="card lg:col-span-2">
          <table className="w-full text-left">
            <thead>
              <tr className="border-b text-slate-500"><th>Number</th><th>Title</th><th>Status</th><th>Actions</th></tr>
            </thead>
            <tbody>
              {cases.map((c) => (
                <tr key={c.id} className="border-b">
                  <td className="py-3">{c.caseNumber}</td>
                  <td>{c.title}</td>
                  <td>{c.status}</td>
                  <td className="space-x-2 py-3">
                    <button className="btn btn-secondary" onClick={() => { setEditingId(c.id); setForm(c) }}>Edit</button>
                    <button className="btn btn-secondary" onClick={() => deleteCase(c.id).then(load)}>Delete</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
