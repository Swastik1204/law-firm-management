import axios from 'axios'

const API_BASE_URL = `${import.meta.env.VITE_API_URL ?? 'http://localhost:8081'}/api`

const api = axios.create({
  baseURL: API_BASE_URL
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token && config.url !== '/auth/login') {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export const login = (email: string, password: string) => api.post('/auth/login', { email, password })
export const getDashboard = () => api.get('/dashboard')
export const getClients = () => api.get('/clients')
export const createClient = (payload: any) => api.post('/clients', payload)
export const updateClient = (id: number, payload: any) => api.put(`/clients/${id}`, payload)
export const deleteClient = (id: number) => api.delete(`/clients/${id}`)
export const getLawyers = () => api.get('/lawyers')
export const createLawyer = (payload: any) => api.post('/lawyers', payload)
export const updateLawyer = (id: number, payload: any) => api.put(`/lawyers/${id}`, payload)
export const deleteLawyer = (id: number) => api.delete(`/lawyers/${id}`)
export const getCases = () => api.get('/cases')
export const createCase = (payload: any) => api.post('/cases', payload)
export const updateCase = (id: number, payload: any) => api.put(`/cases/${id}`, payload)
export const deleteCase = (id: number) => api.delete(`/cases/${id}`)
export const getAppointments = () => api.get('/appointments')
export const createAppointment = (payload: any) => api.post('/appointments', payload)
export const updateAppointment = (id: number, payload: any) => api.put(`/appointments/${id}`, payload)
export const getDocuments = () => api.get('/documents')
export const uploadDocument = (form: FormData) => api.post('/documents', form, { headers: { 'Content-Type': 'multipart/form-data' } })
export const deleteDocument = (id: number) => api.delete(`/documents/${id}`)

export default api
