import { useEffect, useState } from 'react'
import { deleteDocument, getDocuments, uploadDocument } from '../api'
import type { DocumentItem } from '../types'

export default function DocumentsPage() {
  const [documents, setDocuments] = useState<DocumentItem[]>([])
  const [file, setFile] = useState<File | null>(null)
  const [clientId, setClientId] = useState('')
  const [caseId, setCaseId] = useState('')

  const load = async () => {
    const res = await getDocuments()
    setDocuments(res.data)
  }

  useEffect(() => { load() }, [])

  const submit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!file) return
    const form = new FormData()
    form.append('file', file)
    form.append('clientId', clientId)
    form.append('caseId', caseId)
    form.append('uploadedBy', 'admin@lawfirm.com')
    await uploadDocument(form)
    setFile(null)
    setClientId('')
    setCaseId('')
    load()
  }

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold">Documents</h2>
      <form className="card space-y-3" onSubmit={submit}>
        <input className="input" type="file" onChange={(e) => setFile(e.target.files?.[0] || null)} />
        <input className="input" placeholder="Client ID" value={clientId} onChange={(e) => setClientId(e.target.value)} />
        <input className="input" placeholder="Case ID (optional)" value={caseId} onChange={(e) => setCaseId(e.target.value)} />
        <button className="btn btn-primary" type="submit">Upload document</button>
      </form>
      <div className="card">
        <table className="w-full text-left">
          <thead>
            <tr className="border-b text-slate-500"><th>Name</th><th>Type</th><th>Size</th><th>Actions</th></tr>
          </thead>
          <tbody>
            {documents.map((doc) => (
              <tr key={doc.id} className="border-b">
                <td className="py-3">{doc.originalName}</td>
                <td>{doc.mimeType}</td>
                <td>{Math.round(doc.fileSize / 1024)} KB</td>
                <td><button className="btn btn-secondary" onClick={() => deleteDocument(doc.id).then(load)}>Delete</button></td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
