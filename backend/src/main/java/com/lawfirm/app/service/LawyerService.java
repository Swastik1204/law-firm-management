package com.lawfirm.app.service;

import com.lawfirm.app.dto.LawyerDto;
import com.lawfirm.app.entity.Lawyer;
import com.lawfirm.app.repository.LawyerRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class LawyerService {
    private final LawyerRepository lawyerRepository;

    public LawyerService(LawyerRepository lawyerRepository) {
        this.lawyerRepository = lawyerRepository;
    }

    public List<LawyerDto> findAll() {
        return lawyerRepository.findAll().stream().map(this::toDto).collect(Collectors.toList());
    }

    public LawyerDto save(LawyerDto dto) {
        Lawyer lawyer = dto.getId() != null ? lawyerRepository.findById(dto.getId()).orElse(new Lawyer()) : new Lawyer();
        lawyer.setFullName(dto.getFullName());
        lawyer.setEmail(dto.getEmail());
        lawyer.setPhone(dto.getPhone());
        lawyer.setSpecialization(dto.getSpecialization());
        lawyer.setYearsOfExperience(dto.getYearsOfExperience());
        lawyer.setBarRegistrationNumber(dto.getBarRegistrationNumber());
        lawyer.setAvailabilityStatus(dto.getAvailabilityStatus());
        return toDto(lawyerRepository.save(lawyer));
    }

    public LawyerDto findById(Long id) {
        return toDto(lawyerRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("Lawyer not found")));
    }

    public void delete(Long id) {
        lawyerRepository.deleteById(id);
    }

    public Lawyer findEntityById(Long id) {
        return lawyerRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("Lawyer not found"));
    }

    private LawyerDto toDto(Lawyer lawyer) {
        LawyerDto dto = new LawyerDto();
        dto.setId(lawyer.getId());
        dto.setFullName(lawyer.getFullName());
        dto.setEmail(lawyer.getEmail());
        dto.setPhone(lawyer.getPhone());
        dto.setSpecialization(lawyer.getSpecialization());
        dto.setYearsOfExperience(lawyer.getYearsOfExperience());
        dto.setBarRegistrationNumber(lawyer.getBarRegistrationNumber());
        dto.setAvailabilityStatus(lawyer.getAvailabilityStatus());
        return dto;
    }
}
