package com.lawfirm.app.config;

import com.lawfirm.app.entity.ActivityLog;
import com.lawfirm.app.entity.Appointment;
import com.lawfirm.app.entity.AppointmentStatus;
import com.lawfirm.app.entity.CaseStatus;
import com.lawfirm.app.entity.Client;
import com.lawfirm.app.entity.Lawyer;
import com.lawfirm.app.entity.LegalCase;
import com.lawfirm.app.entity.RoleName;
import com.lawfirm.app.entity.User;
import com.lawfirm.app.repository.ActivityLogRepository;
import com.lawfirm.app.repository.AppointmentRepository;
import com.lawfirm.app.repository.ClientRepository;
import com.lawfirm.app.repository.LawyerRepository;
import com.lawfirm.app.repository.LegalCaseRepository;
import com.lawfirm.app.repository.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import java.time.LocalDate;
import java.time.LocalTime;

@Component
public class DataSeeder implements CommandLineRunner {
    private final UserRepository userRepository;
    private final ClientRepository clientRepository;
    private final LawyerRepository lawyerRepository;
    private final LegalCaseRepository legalCaseRepository;
    private final AppointmentRepository appointmentRepository;
    private final ActivityLogRepository activityLogRepository;
    private final PasswordEncoder passwordEncoder;

    public DataSeeder(UserRepository userRepository, ClientRepository clientRepository, LawyerRepository lawyerRepository,
                      LegalCaseRepository legalCaseRepository, AppointmentRepository appointmentRepository,
                      ActivityLogRepository activityLogRepository, PasswordEncoder passwordEncoder) {
        this.userRepository = userRepository;
        this.clientRepository = clientRepository;
        this.lawyerRepository = lawyerRepository;
        this.legalCaseRepository = legalCaseRepository;
        this.appointmentRepository = appointmentRepository;
        this.activityLogRepository = activityLogRepository;
        this.passwordEncoder = passwordEncoder;
    }

    @Override
    public void run(String... args) {
        if (userRepository.count() == 0) {
            User admin = new User("Admin", "User", "admin@lawfirm.com", passwordEncoder.encode("Admin@123"), "+1-555-0101", RoleName.ADMIN);
            userRepository.save(admin);

            Client c1 = new Client();
            c1.setFullName("Aisha Rahman");
            c1.setEmail("aisha@example.com");
            c1.setPhone("+1-555-0202");
            c1.setAddress("12 Cedar Lane, Mumbai");
            c1.setClientType("Corporate");
            c1.setNotes("High priority contract dispute");
            clientRepository.save(c1);

            Client c2 = new Client();
            c2.setFullName("Ravi Sharma");
            c2.setEmail("ravi@example.com");
            c2.setPhone("+1-555-0303");
            c2.setAddress("7 River Road, Pune");
            c2.setClientType("Individual");
            c2.setNotes("Family law consultation");
            clientRepository.save(c2);

            Lawyer l1 = new Lawyer();
            l1.setFullName("Priya Nair");
            l1.setEmail("priya@lawfirm.com");
            l1.setPhone("+1-555-0404");
            l1.setSpecialization("Corporate Law");
            l1.setYearsOfExperience(8);
            l1.setBarRegistrationNumber("BAR-1204");
            l1.setAvailabilityStatus("Available");
            lawyerRepository.save(l1);

            Lawyer l2 = new Lawyer();
            l2.setFullName("Harsh Mehta");
            l2.setEmail("harsh@lawfirm.com");
            l2.setPhone("+1-555-0505");
            l2.setSpecialization("Family Law");
            l2.setYearsOfExperience(11);
            l2.setBarRegistrationNumber("BAR-9901");
            l2.setAvailabilityStatus("On Call");
            lawyerRepository.save(l2);

            LegalCase legalCase = new LegalCase();
            legalCase.setCaseNumber("LF-2026-001");
            legalCase.setTitle("Corporate Contract Review");
            legalCase.setCaseType("Commercial Litigation");
            legalCase.setClient(c1);
            legalCase.setCourtName("High Court of Mumbai");
            legalCase.setFilingDate(LocalDate.now().minusDays(12));
            legalCase.setNextHearingDate(LocalDate.now().plusDays(10));
            legalCase.setDescription("Review and enforcement of contract terms after termination dispute.");
            legalCase.setStatus(CaseStatus.ACTIVE);
            legalCase.getLawyers().add(l1);
            legalCaseRepository.save(legalCase);

            Appointment ap1 = new Appointment();
            ap1.setClient(c1);
            ap1.setLawyer(l1);
            ap1.setLegalCase(legalCase);
            ap1.setDate(LocalDate.now().plusDays(2));
            ap1.setTime(LocalTime.of(11, 0));
            ap1.setLocation("Conference Room A");
            ap1.setAppointmentType("Hearing");
            ap1.setDescription("Client strategy meeting");
            ap1.setStatus(AppointmentStatus.SCHEDULED);
            appointmentRepository.save(ap1);

            activityLogRepository.save(new ActivityLog("System", "Seed Data", "Default admin and sample records initialized."));
        }
    }
}
