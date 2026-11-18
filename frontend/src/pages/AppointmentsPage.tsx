import { useEffect, useState } from 'react'
import { createAppointment, getAppointments, updateAppointment } from '../api'
import type { Appointment } from '../types'

const empty: Omit<Appointment, 'id' | 'clientName' | 'lawyerName'> = {
  clientId: 0, lawyerId: 0, caseId: 0, date: '', time: '', location: '', appointmentType: 'Hearing', description: '', status: 'SCHEDULED'
}

export default function AppointmentsPage() {
  const [items, setItems] = useState<Appointment[]>([])
  const [form, setForm] = useState(empty)

  const load = async () => {
    const res = await getAppointments()
    setItems(res.data)
  }

  useEffect(() => { load() }, [])

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    await createAppointment(form)
    setForm(empty)
    load()
  }

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold">Appointments</h2>
      <div className="grid lg:grid-cols-3 gap-6">
        <form className="card lg:col-span-1 space-y-3" onSubmit={submit}>
          <input className="input" type="number" placeholder="Client ID" value={form.clientId} onChange={(e) => setForm({ ...form, clientId: Number(e.target.value) })} />
          <input className="input" type="number" placeholder="Lawyer ID" value={form.lawyerId} onChange={(e) => setForm({ ...form, lawyerId: Number(e.target.value) })} />
          <input className="input" type="number" placeholder="Case ID" value={form.caseId || 0} onChange={(e) => setForm({ ...form, caseId: Number(e.target.value) })} />
          <input className="input" type="date" value={form.date} onChange={(e) => setForm({ ...form, date: e.target.value })} />
          <input className="input" type="time" value={form.time} onChange={(e) => setForm({ ...form, time: e.target.value })} />
          <input className="input" placeholder="Location" value={form.location} onChange={(e) => setForm({ ...form, location: e.target.value })} />
          <input className="input" placeholder="Type" value={form.appointmentType} onChange={(e) => setForm({ ...form, appointmentType: e.target.value })} />
          <input className="input" placeholder="Description" value={form.description} onChange={(e) => setForm({ ...form, description: e.target.value })} />
          <input className="input" placeholder="Status" value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value })} />
          <button className="btn btn-primary w-full" type="submit">Save Appointment</button>
        </form>
        <div className="card lg:col-span-2">
          <table className="w-full text-left">
            <thead>
              <tr className="border-b text-slate-500"><th>Client</th><th>Lawyer</th><th>Date</th><th>Status</th></tr>
            </thead>
            <tbody>
              {items.map((item) => (
                <tr key={item.id} className="border-b">
                  <td className="py-3">{item.clientName}</td>
                  <td>{item.lawyerName}</td>
                  <td>{item.date}</td>
                  <td>{item.status}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  )
}
