import { useEffect, useState } from 'react'
import { createLawyer, deleteLawyer, getLawyers, updateLawyer } from '../api'
import type { Lawyer } from '../types'

const empty: Omit<Lawyer, 'id'> = {
  fullName: '', email: '', phone: '', specialization: '', yearsOfExperience: 0, barRegistrationNumber: '', availabilityStatus: 'Available'
}

export default function LawyersPage() {
  const [lawyers, setLawyers] = useState<Lawyer[]>([])
  const [form, setForm] = useState(empty)
  const [editingId, setEditingId] = useState<number | null>(null)

  const load = async () => {
    const res = await getLawyers()
    setLawyers(res.data)
  }

  useEffect(() => { load() }, [])

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (editingId) await updateLawyer(editingId, form)
    else await createLawyer(form)
    setForm(empty)
    setEditingId(null)
    load()
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-3xl font-bold">Lawyers</h2>
        <button className="btn btn-primary" onClick={() => setForm(empty)}>New Lawyer</button>
      </div>
      <div className="grid lg:grid-cols-3 gap-6">
        <form className="card lg:col-span-1 space-y-3" onSubmit={submit}>
          <h3 className="text-xl font-semibold">{editingId ? 'Edit Lawyer' : 'Add Lawyer'}</h3>
          <input className="input" placeholder="Full name" value={form.fullName} onChange={(e) => setForm({ ...form, fullName: e.target.value })} />
          <input className="input" placeholder="Email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
          <input className="input" placeholder="Phone" value={form.phone} onChange={(e) => setForm({ ...form, phone: e.target.value })} />
          <input className="input" placeholder="Specialization" value={form.specialization} onChange={(e) => setForm({ ...form, specialization: e.target.value })} />
          <input className="input" type="number" placeholder="Experience years" value={form.yearsOfExperience} onChange={(e) => setForm({ ...form, yearsOfExperience: Number(e.target.value) })} />
          <input className="input" placeholder="Bar number" value={form.barRegistrationNumber} onChange={(e) => setForm({ ...form, barRegistrationNumber: e.target.value })} />
          <input className="input" placeholder="Availability" value={form.availabilityStatus} onChange={(e) => setForm({ ...form, availabilityStatus: e.target.value })} />
          <button className="btn btn-primary w-full">Save</button>
        </form>
        <div className="card lg:col-span-2">
          <table className="w-full text-left">
            <thead>
              <tr className="border-b text-slate-500">
                <th>Name</th><th>Specialization</th><th>Years</th><th>Status</th><th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {lawyers.map((lawyer) => (
                <tr key={lawyer.id} className="border-b">
                  <td className="py-3">{lawyer.fullName}</td>
                  <td>{lawyer.specialization}</td>
                  <td>{lawyer.yearsOfExperience}</td>
                  <td>{lawyer.availabilityStatus}</td>
                  <td className="space-x-2 py-3">
                    <button className="btn btn-secondary" onClick={() => { setEditingId(lawyer.id); setForm(lawyer) }}>Edit</button>
                    <button className="btn btn-secondary" onClick={() => deleteLawyer(lawyer.id).then(load)}>Delete</button>
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
