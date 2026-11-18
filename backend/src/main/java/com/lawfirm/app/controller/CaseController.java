package com.lawfirm.app.controller;

import com.lawfirm.app.dto.LegalCaseDto;
import com.lawfirm.app.service.CaseService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/cases")
@CrossOrigin(origins = "*")
public class CaseController {
    private final CaseService caseService;

    public CaseController(CaseService caseService) {
        this.caseService = caseService;
    }

    @GetMapping
    public ResponseEntity<List<LegalCaseDto>> all() {
        return ResponseEntity.ok(caseService.findAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<LegalCaseDto> get(@PathVariable Long id) {
        return ResponseEntity.ok(caseService.findById(id));
    }

    @PostMapping
    public ResponseEntity<LegalCaseDto> create(@RequestBody LegalCaseDto dto) {
        return ResponseEntity.status(HttpStatus.CREATED).body(caseService.save(dto));
    }

    @PutMapping("/{id}")
    public ResponseEntity<LegalCaseDto> update(@PathVariable Long id, @RequestBody LegalCaseDto dto) {
        dto.setId(id);
        return ResponseEntity.ok(caseService.save(dto));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        caseService.delete(id);
        return ResponseEntity.noContent().build();
    }
}
