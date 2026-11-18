package com.lawfirm.app.service;

import com.lawfirm.app.dto.LegalCaseDto;
import com.lawfirm.app.entity.CaseStatus;
import com.lawfirm.app.entity.Client;
import com.lawfirm.app.entity.Lawyer;
import com.lawfirm.app.entity.LegalCase;
import com.lawfirm.app.repository.ClientRepository;
import com.lawfirm.app.repository.LegalCaseRepository;
import org.springframework.stereotype.Service;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

@Service
public class CaseService {
    private final LegalCaseRepository legalCaseRepository;
    private final ClientRepository clientRepository;
    private final LawyerService lawyerService;

    public CaseService(LegalCaseRepository legalCaseRepository, ClientRepository clientRepository, LawyerService lawyerService) {
        this.legalCaseRepository = legalCaseRepository;
        this.clientRepository = clientRepository;
        this.lawyerService = lawyerService;
    }

    public List<LegalCaseDto> findAll() {
        return legalCaseRepository.findAll().stream().map(this::toDto).collect(Collectors.toList());
    }

    public LegalCaseDto save(LegalCaseDto dto) {
        LegalCase legalCase = dto.getId() != null ? legalCaseRepository.findById(dto.getId()).orElse(new LegalCase()) : new LegalCase();
        Client client = clientRepository.findById(dto.getClientId()).orElseThrow(() -> new IllegalArgumentException("Client not found"));
        legalCase.setClient(client);
        legalCase.setCaseNumber(dto.getCaseNumber());
        legalCase.setTitle(dto.getTitle());
        legalCase.setCaseType(dto.getCaseType());
        legalCase.setCourtName(dto.getCourtName());
        legalCase.setFilingDate(dto.getFilingDate());
        legalCase.setNextHearingDate(dto.getNextHearingDate());
        legalCase.setDescription(dto.getDescription());
        if (dto.getStatus() != null) {
            legalCase.setStatus(CaseStatus.valueOf(dto.getStatus().toUpperCase().replace(' ', '_')));
        }

        Set<Lawyer> lawyers = new HashSet<>();
        if (dto.getLawyerIds() != null) {
            for (Long lawyerId : dto.getLawyerIds()) {
                lawyers.add(lawyerService.findEntityById(lawyerId));
            }
        }
        legalCase.setLawyers(lawyers);
        return toDto(legalCaseRepository.save(legalCase));
    }

    public LegalCaseDto findById(Long id) {
        return toDto(legalCaseRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("Case not found")));
    }

    public void delete(Long id) {
        legalCaseRepository.deleteById(id);
    }

    private LegalCaseDto toDto(LegalCase legalCase) {
        LegalCaseDto dto = new LegalCaseDto();
        dto.setId(legalCase.getId());
        dto.setCaseNumber(legalCase.getCaseNumber());
        dto.setTitle(legalCase.getTitle());
        dto.setCaseType(legalCase.getCaseType());
        dto.setClientId(legalCase.getClient() != null ? legalCase.getClient().getId() : null);
        dto.setClientName(legalCase.getClient() != null ? legalCase.getClient().getFullName() : null);
        dto.setCourtName(legalCase.getCourtName());
        dto.setFilingDate(legalCase.getFilingDate());
        dto.setNextHearingDate(legalCase.getNextHearingDate());
        dto.setDescription(legalCase.getDescription());
        dto.setStatus(legalCase.getStatus().name());
        if (legalCase.getLawyers() != null) {
            dto.setLawyerIds(legalCase.getLawyers().stream().map(Lawyer::getId).collect(Collectors.toSet()));
        }
        return dto;
    }
}
