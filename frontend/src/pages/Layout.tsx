import { BarChart3, BriefcaseBusiness, CalendarDays, FolderOpen, Gavel, LogOut, Users } from 'lucide-react'
import { Link, useLocation, useNavigate } from 'react-router-dom'

const navItems = [
  { label: 'Dashboard', to: '/', icon: BarChart3 },
  { label: 'Clients', to: '/clients', icon: Users },
  { label: 'Lawyers', to: '/lawyers', icon: Gavel },
  { label: 'Cases', to: '/cases', icon: BriefcaseBusiness },
  { label: 'Appointments', to: '/appointments', icon: CalendarDays },
  { label: 'Documents', to: '/documents', icon: FolderOpen },
]

export default function Layout({ children }: { children: React.ReactNode }) {
  const navigate = useNavigate()
  const location = useLocation()

  const handleLogout = () => {
    localStorage.removeItem('token')
    navigate('/login')
  }

  return (
    <div className="min-h-screen bg-slate-100">
      <div className="flex">
        <aside className="h-screen w-72 bg-slate-900 text-slate-100 p-5">
          <h1 className="mb-8 text-2xl font-bold">LegalFlow</h1>
          <nav className="space-y-2">
            {navItems.map(({ label, to, icon: Icon }) => (
              <Link
                key={to}
                to={to}
                className={`flex items-center gap-3 rounded-xl px-3 py-3 ${location.pathname === to ? 'bg-slate-700' : 'hover:bg-slate-800'}`}
              >
                <Icon size={18} />
                {label}
              </Link>
            ))}
          </nav>
          <button className="mt-8 flex w-full items-center gap-3 rounded-xl bg-slate-800 px-3 py-3 hover:bg-slate-700" onClick={handleLogout}>
            <LogOut size={18} />
            Logout
          </button>
        </aside>
        <main className="flex-1 p-6">{children}</main>
      </div>
    </div>
  )
}
