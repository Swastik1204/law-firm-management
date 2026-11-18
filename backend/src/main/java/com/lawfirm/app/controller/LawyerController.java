package com.lawfirm.app.controller;

import com.lawfirm.app.dto.LawyerDto;
import com.lawfirm.app.service.LawyerService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/lawyers")
@CrossOrigin(origins = "*")
public class LawyerController {
    private final LawyerService lawyerService;

    public LawyerController(LawyerService lawyerService) {
        this.lawyerService = lawyerService;
    }

    @GetMapping
    public ResponseEntity<List<LawyerDto>> all() {
        return ResponseEntity.ok(lawyerService.findAll());
    }

    @PostMapping
    public ResponseEntity<LawyerDto> create(@RequestBody LawyerDto dto) {
        return ResponseEntity.status(HttpStatus.CREATED).body(lawyerService.save(dto));
    }

    @PutMapping("/{id}")
    public ResponseEntity<LawyerDto> update(@PathVariable Long id, @RequestBody LawyerDto dto) {
        dto.setId(id);
        return ResponseEntity.ok(lawyerService.save(dto));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        lawyerService.delete(id);
        return ResponseEntity.noContent().build();
    }
}
