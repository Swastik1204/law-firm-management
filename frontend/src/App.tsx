import { Navigate, Route, Routes } from 'react-router-dom'
import LoginPage from './pages/LoginPage'
import DashboardPage from './pages/DashboardPage'
import ClientsPage from './pages/ClientsPage'
import LawyersPage from './pages/LawyersPage'
import CasesPage from './pages/CasesPage'
import AppointmentsPage from './pages/AppointmentsPage'
import DocumentsPage from './pages/DocumentsPage'
import Layout from './pages/Layout'

const isAuthenticated = () => Boolean(localStorage.getItem('token'))

export default function App() {
  return (
    <Routes>
      <Route path="/login" element={<LoginPage />} />
      <Route
        path="/"
        element={isAuthenticated() ? <Layout><DashboardPage /></Layout> : <Navigate to="/login" replace />}
      />
      <Route
        path="/clients"
        element={isAuthenticated() ? <Layout><ClientsPage /></Layout> : <Navigate to="/login" replace />}
      />
      <Route
        path="/lawyers"
        element={isAuthenticated() ? <Layout><LawyersPage /></Layout> : <Navigate to="/login" replace />}
      />
      <Route
        path="/cases"
        element={isAuthenticated() ? <Layout><CasesPage /></Layout> : <Navigate to="/login" replace />}
      />
      <Route
        path="/appointments"
        element={isAuthenticated() ? <Layout><AppointmentsPage /></Layout> : <Navigate to="/login" replace />}
      />
      <Route
        path="/documents"
        element={isAuthenticated() ? <Layout><DocumentsPage /></Layout> : <Navigate to="/login" replace />}
      />
      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
