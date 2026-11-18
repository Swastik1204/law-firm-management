package com.lawfirm.app.service;

import com.lawfirm.app.dto.DocumentDto;
import com.lawfirm.app.entity.Client;
import com.lawfirm.app.entity.DocumentRecord;
import com.lawfirm.app.entity.LegalCase;
import com.lawfirm.app.repository.ClientRepository;
import com.lawfirm.app.repository.DocumentRepository;
import com.lawfirm.app.repository.LegalCaseRepository;
import com.lawfirm.app.storage.StorageService;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class DocumentService {
    private final DocumentRepository documentRepository;
    private final ClientRepository clientRepository;
    private final LegalCaseRepository legalCaseRepository;
    private final StorageService storageService;

    public DocumentService(DocumentRepository documentRepository, ClientRepository clientRepository, LegalCaseRepository legalCaseRepository, StorageService storageService) {
        this.documentRepository = documentRepository;
        this.clientRepository = clientRepository;
        this.legalCaseRepository = legalCaseRepository;
        this.storageService = storageService;
    }

    public List<DocumentDto> findAll() {
        return documentRepository.findAll().stream().map(this::toDto).collect(Collectors.toList());
    }

    public DocumentDto upload(MultipartFile file, Long clientId, Long caseId, String uploadedBy) {
        if (file == null || file.isEmpty()) {
            throw new IllegalArgumentException("No file selected");
        }
        String mimeType = file.getContentType() == null ? "application/octet-stream" : file.getContentType();
        if (!isAllowedMime(mimeType)) {
            throw new IllegalArgumentException("Unsupported document type");
        }
        Client client = clientRepository.findById(clientId).orElseThrow(() -> new IllegalArgumentException("Client not found"));
        LegalCase legalCase = caseId != null ? legalCaseRepository.findById(caseId).orElseThrow(() -> new IllegalArgumentException("Case not found")) : null;

        String storedPath = storageService.store(file, "documents");
        DocumentRecord record = new DocumentRecord();
        record.setFileName(file.getOriginalFilename());
        record.setOriginalName(file.getOriginalFilename());
        record.setMimeType(mimeType);
        record.setFileSize(file.getSize());
        record.setStoredPath(storedPath);
        record.setClient(client);
        record.setLegalCase(legalCase);
        record.setUploadedBy(uploadedBy);

        DocumentRecord saved = documentRepository.save(record);
        return toDto(saved);
    }

    public void delete(Long id) {
        DocumentRecord document = documentRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("Document not found"));
        storageService.deleteFile(document.getStoredPath());
        documentRepository.delete(document);
    }

    private boolean isAllowedMime(String mimeType) {
        return mimeType != null && (mimeType.equals("application/pdf")
            || mimeType.equals("application/msword")
            || mimeType.equals("application/vnd.openxmlformats-officedocument.wordprocessingml.document")
            || mimeType.startsWith("image/")
            || mimeType.equals("application/vnd.ms-excel")
            || mimeType.equals("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"));
    }

    private DocumentDto toDto(DocumentRecord record) {
        DocumentDto dto = new DocumentDto();
        dto.setId(record.getId());
        dto.setFileName(record.getFileName());
        dto.setOriginalName(record.getOriginalName());
        dto.setMimeType(record.getMimeType());
        dto.setFileSize(record.getFileSize());
        dto.setUploadedAt(record.getUploadedAt());
        dto.setUploadedBy(record.getUploadedBy());
        dto.setCaseId(record.getLegalCase() != null ? record.getLegalCase().getId() : null);
        dto.setClientId(record.getClient() != null ? record.getClient().getId() : null);
        return dto;
    }
}
