package com.lawfirm.app.controller;

import com.lawfirm.app.dto.DocumentDto;
import com.lawfirm.app.service.DocumentService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@RestController
@RequestMapping("/api/documents")
@CrossOrigin(origins = "*")
public class DocumentController {
    private final DocumentService documentService;

    public DocumentController(DocumentService documentService) {
        this.documentService = documentService;
    }

    @GetMapping
    public ResponseEntity<List<DocumentDto>> all() {
        return ResponseEntity.ok(documentService.findAll());
    }

    @PostMapping
    public ResponseEntity<DocumentDto> upload(@RequestParam("file") MultipartFile file,
                                            @RequestParam("clientId") Long clientId,
                                            @RequestParam(value = "caseId", required = false) Long caseId,
                                            @RequestParam("uploadedBy") String uploadedBy) {
        return ResponseEntity.status(HttpStatus.CREATED).body(documentService.upload(file, clientId, caseId, uploadedBy));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        documentService.delete(id);
        return ResponseEntity.noContent().build();
    }
}
