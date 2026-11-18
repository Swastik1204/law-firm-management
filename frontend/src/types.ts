export type Role = 'ADMIN' | 'LAWYER' | 'STAFF'

export type AuthResponse = {
  token: string
  email: string
  role: Role
  userId: number
}

export type Client = {
  id: number
  fullName: string
  email: string
  phone: string
  address: string
  dateOfRegistration?: string
  clientType: string
  notes: string
}

export type Lawyer = {
  id: number
  fullName: string
  email: string
  phone: string
  specialization: string
  yearsOfExperience: number
  barRegistrationNumber: string
  availabilityStatus: string
}

export type CaseItem = {
  id: number
  caseNumber: string
  title: string
  caseType: string
  clientId: number
  clientName: string
  lawyerIds?: number[]
  courtName: string
  filingDate: string
  nextHearingDate?: string
  description: string
  status: string
}

export type Appointment = {
  id: number
  clientId: number
  clientName: string
  lawyerId: number
  lawyerName: string
  caseId?: number
  date: string
  time: string
  location: string
  appointmentType: string
  description: string
  status: string
}

export type DocumentItem = {
  id: number
  fileName: string
  originalName: string
  mimeType: string
  fileSize: number
  uploadedAt: string
  uploadedBy: string
  caseId?: number
  clientId: number
}

export type ActivityLog = {
  id: number
  actor: string
  action: string
  details: string
  createdAt: string
}

export type DashboardData = {
  totalClients: number
  totalLawyers: number
  totalActiveCases: number
  totalClosedCases: number
  upcomingHearings: number
  todaysAppointments: number
  recentCases: CaseItem[]
  recentActivities: ActivityLog[]
  caseStatusDistribution: Record<string, number>
  monthlyCaseRegistrations: Array<{ month: string; count: number }>
}
