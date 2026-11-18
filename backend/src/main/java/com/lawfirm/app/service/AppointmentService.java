package com.lawfirm.app.service;

import com.lawfirm.app.dto.AppointmentDto;
import com.lawfirm.app.entity.Appointment;
import com.lawfirm.app.entity.AppointmentStatus;
import com.lawfirm.app.entity.Client;
import com.lawfirm.app.entity.Lawyer;
import com.lawfirm.app.entity.LegalCase;
import com.lawfirm.app.repository.AppointmentRepository;
import com.lawfirm.app.repository.ClientRepository;
import com.lawfirm.app.repository.LegalCaseRepository;
import com.lawfirm.app.repository.LawyerRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class AppointmentService {
    private final AppointmentRepository appointmentRepository;
    private final ClientRepository clientRepository;
    private final LawyerRepository lawyerRepository;
    private final LegalCaseRepository legalCaseRepository;

    public AppointmentService(AppointmentRepository appointmentRepository, ClientRepository clientRepository, LawyerRepository lawyerRepository, LegalCaseRepository legalCaseRepository) {
        this.appointmentRepository = appointmentRepository;
        this.clientRepository = clientRepository;
        this.lawyerRepository = lawyerRepository;
        this.legalCaseRepository = legalCaseRepository;
    }

    public List<AppointmentDto> findAll() {
        return appointmentRepository.findAll().stream().map(this::toDto).collect(Collectors.toList());
    }

    public AppointmentDto save(AppointmentDto dto) {
        Appointment appointment = dto.getId() != null ? appointmentRepository.findById(dto.getId()).orElse(new Appointment()) : new Appointment();
        Client client = clientRepository.findById(dto.getClientId()).orElseThrow(() -> new IllegalArgumentException("Client not found"));
        Lawyer lawyer = lawyerRepository.findById(dto.getLawyerId()).orElseThrow(() -> new IllegalArgumentException("Lawyer not found"));
        LegalCase legalCase = dto.getCaseId() != null ? legalCaseRepository.findById(dto.getCaseId()).orElse(null) : null;

        appointment.setClient(client);
        appointment.setLawyer(lawyer);
        appointment.setLegalCase(legalCase);
        appointment.setDate(dto.getDate());
        appointment.setTime(dto.getTime());
        appointment.setLocation(dto.getLocation());
        appointment.setAppointmentType(dto.getAppointmentType());
        appointment.setDescription(dto.getDescription());
        if (dto.getStatus() != null) {
            appointment.setStatus(AppointmentStatus.valueOf(dto.getStatus().toUpperCase()));
        }

        return toDto(appointmentRepository.save(appointment));
    }

    private AppointmentDto toDto(Appointment appointment) {
        AppointmentDto dto = new AppointmentDto();
        dto.setId(appointment.getId());
        dto.setClientId(appointment.getClient() != null ? appointment.getClient().getId() : null);
        dto.setClientName(appointment.getClient() != null ? appointment.getClient().getFullName() : null);
        dto.setLawyerId(appointment.getLawyer() != null ? appointment.getLawyer().getId() : null);
        dto.setLawyerName(appointment.getLawyer() != null ? appointment.getLawyer().getFullName() : null);
        dto.setCaseId(appointment.getLegalCase() != null ? appointment.getLegalCase().getId() : null);
        dto.setDate(appointment.getDate());
        dto.setTime(appointment.getTime());
        dto.setLocation(appointment.getLocation());
        dto.setAppointmentType(appointment.getAppointmentType());
        dto.setDescription(appointment.getDescription());
        dto.setStatus(appointment.getStatus().name());
        return dto;
    }
}
