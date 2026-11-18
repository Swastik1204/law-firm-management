import { useEffect, useState } from 'react'
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts'
import { getDashboard } from '../api'
import type { DashboardData } from '../types'

const COLORS = ['#2563eb', '#14b8a6', '#f59e0b', '#ef4444', '#8b5cf6', '#10b981']

export default function DashboardPage() {
  const [data, setData] = useState<DashboardData | null>(null)

  useEffect(() => {
    getDashboard().then((res) => setData(res.data)).catch(() => setData(null))
  }, [])

  if (!data) return <div className="card">Loading dashboard…</div>

  const pieData = Object.entries(data.caseStatusDistribution || {}).map(([name, value]) => ({ name, value }))

  return (
    <div className="space-y-6">
      <div>
        <h2 className="text-3xl font-bold">Dashboard</h2>
        <p className="text-slate-500">Overview of legal operations</p>
      </div>

      <div className="grid md:grid-cols-2 xl:grid-cols-6 gap-4">
        {[
          ['Clients', data.totalClients],
          ['Lawyers', data.totalLawyers],
          ['Active Cases', data.totalActiveCases],
          ['Closed Cases', data.totalClosedCases],
          ['Upcoming Hearings', data.upcomingHearings],
          ["Today's Appointments", data.todaysAppointments],
        ].map(([label, value], index) => (
          <div key={label} className="card">
            <div className="text-sm text-slate-500">{label}</div>
            <div className="mt-2 text-3xl font-bold text-slate-800">{value}</div>
            <div className="mt-1 h-1 w-12 rounded bg-blue-500" style={{ opacity: 0.3 + index * 0.1 }} />
          </div>
        ))}
      </div>

      <div className="grid lg:grid-cols-2 gap-6">
        <div className="card">
          <h3 className="mb-4 text-lg font-semibold">Case Status Distribution</h3>
          <ResponsiveContainer width="100%" height={300}>
            <PieChart>
              <Pie data={pieData} dataKey="value" nameKey="name" outerRadius={80} label>
                {pieData.map((_, index) => (
                  <Cell key={index} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
        <div className="card">
          <h3 className="mb-4 text-lg font-semibold">Monthly Case Registrations</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data.monthlyCaseRegistrations || []}>
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="count" fill="#2563eb" radius={[8, 8, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className="grid lg:grid-cols-2 gap-6">
        <div className="card">
          <h3 className="mb-4 text-lg font-semibold">Recent Cases</h3>
          <div className="space-y-3">
            {(data.recentCases || []).slice(0, 5).map((c) => (
              <div key={c.id} className="flex items-center justify-between border-b pb-2">
                <div>
                  <div className="font-medium">{c.title}</div>
                  <div className="text-sm text-slate-500">{c.caseNumber}</div>
                </div>
                <span className="rounded-full bg-blue-100 px-2 py-1 text-xs text-blue-700">{c.status}</span>
              </div>
            ))}
          </div>
        </div>
        <div className="card">
          <h3 className="mb-4 text-lg font-semibold">Recent Activities</h3>
          <div className="space-y-3">
            {(data.recentActivities || []).slice(0, 5).map((a) => (
              <div key={a.id} className="border-b pb-2">
                <div className="font-medium">{a.action}</div>
                <div className="text-sm text-slate-500">{a.actor} · {new Date(a.createdAt).toLocaleString()}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}
