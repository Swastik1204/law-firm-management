import { useEffect, useState } from 'react'
import { deleteClient, getClients, createClient, updateClient } from '../api'
import type { Client } from '../types'

const empty: Omit<Client, 'id'> = {
  fullName: '', email: '', phone: '', address: '', clientType: 'Individual', notes: ''
}

export default function ClientsPage() {
  const [clients, setClients] = useState<Client[]>([])
  const [form, setForm] = useState(empty)
  const [editingId, setEditingId] = useState<number | null>(null)

  const load = async () => {
    const res = await getClients()
    setClients(res.data)
  }

  useEffect(() => { load() }, [])

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (editingId) await updateClient(editingId, form)
    else await createClient(form)
    setForm(empty)
    setEditingId(null)
    load()
  }

  const remove = async (id: number) => {
    await deleteClient(id)
    load()
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-3xl font-bold">Clients</h2>
        <button className="btn btn-primary" onClick={() => setForm(empty)}>New Client</button>
      </div>
      <div className="grid lg:grid-cols-3 gap-6">
        <form className="card lg:col-span-1 space-y-3" onSubmit={submit}>
          <h3 className="text-xl font-semibold">{editingId ? 'Edit Client' : 'Add Client'}</h3>
          <input className="input" placeholder="Full name" value={form.fullName} onChange={(e) => setForm({ ...form, fullName: e.target.value })} />
          <input className="input" placeholder="Email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
          <input className="input" placeholder="Phone" value={form.phone} onChange={(e) => setForm({ ...form, phone: e.target.value })} />
          <input className="input" placeholder="Address" value={form.address} onChange={(e) => setForm({ ...form, address: e.target.value })} />
          <input className="input" placeholder="Client type" value={form.clientType} onChange={(e) => setForm({ ...form, clientType: e.target.value })} />
          <textarea className="input" placeholder="Notes" value={form.notes} onChange={(e) => setForm({ ...form, notes: e.target.value })} />
          <button className="btn btn-primary w-full" type="submit">Save</button>
        </form>

        <div className="card lg:col-span-2">
          <table className="w-full text-left">
            <thead>
              <tr className="border-b text-slate-500">
                <th className="py-2">Name</th>
                <th>Email</th>
                <th>Phone</th>
                <th>Type</th>
                <th>Actions</th>
              </tr>
            </thead>
            <tbody>
              {clients.map((client) => (
                <tr key={client.id} className="border-b">
                  <td className="py-3">{client.fullName}</td>
                  <td>{client.email}</td>
                  <td>{client.phone}</td>
                  <td>{client.clientType}</td>
                  <td className="space-x-2 py-3">
                    <button className="btn btn-secondary" onClick={() => { setEditingId(client.id); setForm(client) }}>Edit</button>
                    <button className="btn btn-secondary" onClick={() => remove(client.id)}>Delete</button>
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
