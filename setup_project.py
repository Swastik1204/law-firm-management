from pathlib import Path
import textwrap

root = Path(r"c:\Users\aggar\Devops Project")

# ---------------------------
# Backend project files
# ---------------------------
backend = root / 'backend'
(base := backend / 'src' / 'main' / 'java' / 'com' / 'lawfirm' / 'app').mkdir(parents=True, exist_ok=True)
for sub in ['config', 'controller', 'dto', 'entity', 'repository', 'security', 'service', 'storage']:
    (base / sub).mkdir(parents=True, exist_ok=True)

# pom
(backend / 'pom.xml').write_text(textwrap.dedent('''
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <parent>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-parent</artifactId>
            <version>3.3.6</version>
            <relativePath/>
        </parent>

        <groupId>com.lawfirm</groupId>
        <artifactId>lawfirm-app</artifactId>
        <version>0.0.1-SNAPSHOT</version>
        <name>lawfirm-app</name>
        <description>Cloud Based Law Firm Management System</description>

        <properties>
            <java.version>17</java.version>
            <maven.compiler.source>17</maven.compiler.source>
            <maven.compiler.target>17</maven.compiler.target>
        </properties>

        <dependencies>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-web</artifactId>
            </dependency>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-data-jpa</artifactId>
            </dependency>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-security</artifactId>
            </dependency>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-validation</artifactId>
            </dependency>
            <dependency>
                <groupId>io.jsonwebtoken</groupId>
                <artifactId>jjwt-api</artifactId>
                <version>0.12.6</version>
            </dependency>
            <dependency>
                <groupId>io.jsonwebtoken</groupId>
                <artifactId>jjwt-impl</artifactId>
                <version>0.12.6</version>
                <scope>runtime</scope>
            </dependency>
            <dependency>
                <groupId>io.jsonwebtoken</groupId>
                <artifactId>jjwt-jackson</artifactId>
                <version>0.12.6</version>
                <scope>runtime</scope>
            </dependency>
            <dependency>
                <groupId>com.h2database</groupId>
                <artifactId>h2</artifactId>
                <scope>runtime</scope>
            </dependency>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-devtools</artifactId>
                <scope>runtime</scope>
                <optional>true</optional>
            </dependency>
            <dependency>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-test</artifactId>
                <scope>test</scope>
            </dependency>
        </dependencies>

        <build>
            <plugins>
                <plugin>
                    <groupId>org.springframework.boot</groupId>
                    <artifactId>spring-boot-maven-plugin</artifactId>
                </plugin>
            </plugins>
        </build>
    </project>
''').strip() + '\n', encoding='utf-8')

# resources
(backend / 'src' / 'main' / 'resources').mkdir(parents=True, exist_ok=True)
(backend / 'src' / 'main' / 'resources' / 'application.properties').write_text(textwrap.dedent('''
    spring.application.name=lawfirm-app
    spring.datasource.url=jdbc:h2:mem:lawfirmdb;MODE=PostgreSQL;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE
    spring.datasource.driver-class-name=org.h2.Driver
    spring.datasource.username=sa
    spring.datasource.password=

    spring.jpa.hibernate.ddl-auto=create-drop
    spring.jpa.show-sql=false
    spring.jpa.properties.hibernate.format_sql=true
    spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.H2Dialect

    spring.h2.console.enabled=true
    spring.h2.console.path=/h2-console
    spring.sql.init.mode=never

    app.jwt.secret=8d4f8f0d9b1c451e8d9d90e4fcf9c9d0
    app.jwt.expiration-ms=86400000
    app.storage.local.path=uploads

    spring.servlet.multipart.max-file-size=10MB
    spring.servlet.multipart.max-request-size=10MB
    server.port=8080
''').strip() + '\n', encoding='utf-8')

(backend / 'src' / 'main' / 'resources' / 'application-docker.properties').write_text(textwrap.dedent('''
    spring.datasource.url=${DATABASE_URL:jdbc:h2:mem:lawfirmdb;MODE=PostgreSQL;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE}
    spring.datasource.driver-class-name=org.h2.Driver
    spring.datasource.username=${DATABASE_USERNAME:sa}
    spring.datasource.password=${DATABASE_PASSWORD:}
    spring.jpa.hibernate.ddl-auto=create-drop
    spring.jpa.show-sql=false
    app.jwt.secret=${APP_JWT_SECRET:8d4f8f0d9b1c451e8d9d90e4fcf9c9d0}
    app.jwt.expiration-ms=86400000
    app.storage.local.path=uploads
''').strip() + '\n', encoding='utf-8')

(backend / 'src' / 'test' / 'resources').mkdir(parents=True, exist_ok=True)
(backend / 'src' / 'test' / 'resources' / 'application.properties').write_text(textwrap.dedent('''
    spring.datasource.url=jdbc:h2:mem:testdb;MODE=PostgreSQL;DB_CLOSE_DELAY=-1;DB_CLOSE_ON_EXIT=FALSE
    spring.datasource.driver-class-name=org.h2.Driver
    spring.datasource.username=sa
    spring.datasource.password=
    spring.jpa.hibernate.ddl-auto=create-drop
    spring.jpa.show-sql=false
    app.jwt.secret=8d4f8f0d9b1c451e8d9d90e4fcf9c9d0
    app.jwt.expiration-ms=86400000
    app.storage.local.path=uploads
''').strip() + '\n', encoding='utf-8')

# utility file writer

def write(path: str, content: str):
    full = base / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(textwrap.dedent(content).strip() + '\n', encoding='utf-8')

# App entry
write('LawFirmApplication.java', '''
package com.lawfirm.app;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class LawFirmApplication {
    public static void main(String[] args) {
        SpringApplication.run(LawFirmApplication.class, args);
    }
}
''')

# config
write('config/SecurityConfig.java', '''
package com.lawfirm.app.config;

import com.lawfirm.app.security.JwtAuthenticationFilter;
import com.lawfirm.app.security.UserDetailsServiceImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.AuthenticationProvider;
import org.springframework.security.authentication.dao.DaoAuthenticationProvider;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
public class SecurityConfig {
    private final UserDetailsServiceImpl userDetailsService;
    private final JwtAuthenticationFilter jwtAuthenticationFilter;

    public SecurityConfig(UserDetailsServiceImpl userDetailsService, JwtAuthenticationFilter jwtAuthenticationFilter) {
        this.userDetailsService = userDetailsService;
        this.jwtAuthenticationFilter = jwtAuthenticationFilter;
    }

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
            .csrf(AbstractHttpConfigurer::disable)
            .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/auth/**", "/h2-console/**").permitAll()
                .requestMatchers("/api/dashboard/**").hasAnyRole("ADMIN", "LAWYER", "STAFF")
                .requestMatchers("/api/clients/**").hasAnyRole("ADMIN", "LAWYER", "STAFF")
                .requestMatchers("/api/lawyers/**").hasAnyRole("ADMIN", "LAWYER", "STAFF")
                .requestMatchers("/api/cases/**").hasAnyRole("ADMIN", "LAWYER", "STAFF")
                .requestMatchers("/api/appointments/**").hasAnyRole("ADMIN", "LAWYER", "STAFF")
                .requestMatchers("/api/documents/**").hasAnyRole("ADMIN", "LAWYER", "STAFF")
                .anyRequest().authenticated())
            .authenticationProvider(authenticationProvider())
            .addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class)
            .headers(headers -> headers.frameOptions(frameOptions -> frameOptions.sameOrigin()));
        return http.build();
    }

    @Bean
    public AuthenticationProvider authenticationProvider() {
        DaoAuthenticationProvider provider = new DaoAuthenticationProvider();
        provider.setUserDetailsService(userDetailsService);
        provider.setPasswordEncoder(passwordEncoder());
        return provider;
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration config) throws Exception {
        return config.getAuthenticationManager();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
''')

write('config/DataSeeder.java', '''
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
''')

# entity
write('entity/RoleName.java', '''
package com.lawfirm.app.entity;

public enum RoleName {
    ADMIN,
    LAWYER,
    STAFF
}
''')
write('entity/User.java', '''
package com.lawfirm.app.entity;

import jakarta.persistence.*;

@Entity
@Table(name = "users")
public class User {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String firstName;

    @Column(nullable = false)
    private String lastName;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(nullable = false)
    private String password;

    @Column(nullable = false)
    private String phone;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private RoleName role;

    @Column(nullable = false)
    private boolean enabled = true;

    public User() {}

    public User(String firstName, String lastName, String email, String password, String phone, RoleName role) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.password = password;
        this.phone = phone;
        this.role = role;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public RoleName getRole() { return role; }
    public void setRole(RoleName role) { this.role = role; }
    public boolean isEnabled() { return enabled; }
    public void setEnabled(boolean enabled) { this.enabled = enabled; }
}
''')
write('entity/Client.java', '''
package com.lawfirm.app.entity;

import jakarta.persistence.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "clients")
public class Client {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String fullName;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(nullable = false)
    private String phone;

    @Column(nullable = false)
    private String address;

    @Column(nullable = false)
    private LocalDate dateOfRegistration = LocalDate.now();

    @Column(nullable = false)
    private String clientType;

    @Column(length = 1000)
    private String notes = "";

    @OneToMany(mappedBy = "client", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<LegalCase> cases = new ArrayList<>();

    public Client() {}

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public LocalDate getDateOfRegistration() { return dateOfRegistration; }
    public void setDateOfRegistration(LocalDate dateOfRegistration) { this.dateOfRegistration = dateOfRegistration; }
    public String getClientType() { return clientType; }
    public void setClientType(String clientType) { this.clientType = clientType; }
    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }
    public List<LegalCase> getCases() { return cases; }
    public void setCases(List<LegalCase> cases) { this.cases = cases; }
}
''')
write('entity/Lawyer.java', '''
package com.lawfirm.app.entity;

import jakarta.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "lawyers")
public class Lawyer {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String fullName;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(nullable = false)
    private String phone;

    @Column(nullable = false)
    private String specialization;

    @Column(nullable = false)
    private int yearsOfExperience;

    @Column(nullable = false)
    private String barRegistrationNumber;

    @Column(nullable = false)
    private String availabilityStatus = "Available";

    @ManyToMany(mappedBy = "lawyers")
    private List<LegalCase> cases = new ArrayList<>();

    public Lawyer() {}

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getSpecialization() { return specialization; }
    public void setSpecialization(String specialization) { this.specialization = specialization; }
    public int getYearsOfExperience() { return yearsOfExperience; }
    public void setYearsOfExperience(int yearsOfExperience) { this.yearsOfExperience = yearsOfExperience; }
    public String getBarRegistrationNumber() { return barRegistrationNumber; }
    public void setBarRegistrationNumber(String barRegistrationNumber) { this.barRegistrationNumber = barRegistrationNumber; }
    public String getAvailabilityStatus() { return availabilityStatus; }
    public void setAvailabilityStatus(String availabilityStatus) { this.availabilityStatus = availabilityStatus; }
    public List<LegalCase> getCases() { return cases; }
    public void setCases(List<LegalCase> cases) { this.cases = cases; }
}
''')
write('entity/CaseStatus.java', '''
package com.lawfirm.app.entity;

public enum CaseStatus {
    PENDING,
    ACTIVE,
    UNDER_REVIEW,
    HEARING_SCHEDULED,
    CLOSED,
    ARCHIVED
}
''')
write('entity/LegalCase.java', '''
package com.lawfirm.app.entity;

import jakarta.persistence.*;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

@Entity
@Table(name = "legal_cases")
public class LegalCase {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true)
    private String caseNumber;

    @Column(nullable = false)
    private String title;

    @Column(nullable = false)
    private String caseType;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "client_id")
    private Client client;

    @ManyToMany
    @JoinTable(
        name = "case_lawyers",
        joinColumns = @JoinColumn(name = "case_id"),
        inverseJoinColumns = @JoinColumn(name = "lawyer_id")
    )
    private Set<Lawyer> lawyers = new HashSet<>();

    @Column(nullable = false)
    private String courtName;

    @Column(nullable = false)
    private LocalDate filingDate;

    private LocalDate nextHearingDate;

    @Column(length = 2000)
    private String description;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private CaseStatus status = CaseStatus.PENDING;

    @OneToMany(mappedBy = "legalCase", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<Appointment> appointments = new ArrayList<>();

    @OneToMany(mappedBy = "legalCase", cascade = CascadeType.ALL, orphanRemoval = true)
    private List<DocumentRecord> documents = new ArrayList<>();

    public LegalCase() {}

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getCaseNumber() { return caseNumber; }
    public void setCaseNumber(String caseNumber) { this.caseNumber = caseNumber; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getCaseType() { return caseType; }
    public void setCaseType(String caseType) { this.caseType = caseType; }
    public Client getClient() { return client; }
    public void setClient(Client client) { this.client = client; }
    public Set<Lawyer> getLawyers() { return lawyers; }
    public void setLawyers(Set<Lawyer> lawyers) { this.lawyers = lawyers; }
    public String getCourtName() { return courtName; }
    public void setCourtName(String courtName) { this.courtName = courtName; }
    public LocalDate getFilingDate() { return filingDate; }
    public void setFilingDate(LocalDate filingDate) { this.filingDate = filingDate; }
    public LocalDate getNextHearingDate() { return nextHearingDate; }
    public void setNextHearingDate(LocalDate nextHearingDate) { this.nextHearingDate = nextHearingDate; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public CaseStatus getStatus() { return status; }
    public void setStatus(CaseStatus status) { this.status = status; }
    public List<Appointment> getAppointments() { return appointments; }
    public void setAppointments(List<Appointment> appointments) { this.appointments = appointments; }
    public List<DocumentRecord> getDocuments() { return documents; }
    public void setDocuments(List<DocumentRecord> documents) { this.documents = documents; }
}
''')
write('entity/AppointmentStatus.java', '''
package com.lawfirm.app.entity;

public enum AppointmentStatus {
    SCHEDULED,
    CONFIRMED,
    CANCELLED,
    COMPLETED
}
''')
write('entity/Appointment.java', '''
package com.lawfirm.app.entity;

import jakarta.persistence.*;
import java.time.LocalDate;
import java.time.LocalTime;

@Entity
@Table(name = "appointments")
public class Appointment {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "client_id", nullable = false)
    private Client client;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "lawyer_id", nullable = false)
    private Lawyer lawyer;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "case_id")
    private LegalCase legalCase;

    @Column(nullable = false)
    private LocalDate date;

    @Column(nullable = false)
    private LocalTime time;

    @Column(nullable = false)
    private String location;

    @Column(nullable = false)
    private String appointmentType;

    @Column(length = 1000)
    private String description;

    @Enumerated(EnumType.STRING)
    @Column(nullable = false)
    private AppointmentStatus status = AppointmentStatus.SCHEDULED;

    public Appointment() {}

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Client getClient() { return client; }
    public void setClient(Client client) { this.client = client; }
    public Lawyer getLawyer() { return lawyer; }
    public void setLawyer(Lawyer lawyer) { this.lawyer = lawyer; }
    public LegalCase getLegalCase() { return legalCase; }
    public void setLegalCase(LegalCase legalCase) { this.legalCase = legalCase; }
    public LocalDate getDate() { return date; }
    public void setDate(LocalDate date) { this.date = date; }
    public LocalTime getTime() { return time; }
    public void setTime(LocalTime time) { this.time = time; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public String getAppointmentType() { return appointmentType; }
    public void setAppointmentType(String appointmentType) { this.appointmentType = appointmentType; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public AppointmentStatus getStatus() { return status; }
    public void setStatus(AppointmentStatus status) { this.status = status; }
}
''')
write('entity/DocumentRecord.java', '''
package com.lawfirm.app.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "documents")
public class DocumentRecord {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String fileName;

    @Column(nullable = false)
    private String originalName;

    @Column(nullable = false)
    private String mimeType;

    @Column(nullable = false)
    private long fileSize;

    @Column(nullable = false)
    private String storedPath;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "client_id")
    private Client client;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "case_id")
    private LegalCase legalCase;

    @Column(nullable = false)
    private LocalDateTime uploadedAt = LocalDateTime.now();

    @Column(nullable = false)
    private String uploadedBy;

    public DocumentRecord() {}

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFileName() { return fileName; }
    public void setFileName(String fileName) { this.fileName = fileName; }
    public String getOriginalName() { return originalName; }
    public void setOriginalName(String originalName) { this.originalName = originalName; }
    public String getMimeType() { return mimeType; }
    public void setMimeType(String mimeType) { this.mimeType = mimeType; }
    public long getFileSize() { return fileSize; }
    public void setFileSize(long fileSize) { this.fileSize = fileSize; }
    public String getStoredPath() { return storedPath; }
    public void setStoredPath(String storedPath) { this.storedPath = storedPath; }
    public Client getClient() { return client; }
    public void setClient(Client client) { this.client = client; }
    public LegalCase getLegalCase() { return legalCase; }
    public void setLegalCase(LegalCase legalCase) { this.legalCase = legalCase; }
    public LocalDateTime getUploadedAt() { return uploadedAt; }
    public void setUploadedAt(LocalDateTime uploadedAt) { this.uploadedAt = uploadedAt; }
    public String getUploadedBy() { return uploadedBy; }
    public void setUploadedBy(String uploadedBy) { this.uploadedBy = uploadedBy; }
}
''')
write('entity/ActivityLog.java', '''
package com.lawfirm.app.entity;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "activity_logs")
public class ActivityLog {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String actor;

    @Column(nullable = false)
    private String action;

    @Column(length = 1000)
    private String details;

    @Column(nullable = false)
    private LocalDateTime createdAt = LocalDateTime.now();

    public ActivityLog() {}

    public ActivityLog(String actor, String action, String details) {
        this.actor = actor;
        this.action = action;
        this.details = details;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getActor() { return actor; }
    public void setActor(String actor) { this.actor = actor; }
    public String getAction() { return action; }
    public void setAction(String action) { this.action = action; }
    public String getDetails() { return details; }
    public void setDetails(String details) { this.details = details; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
''')

# repositories
write('repository/UserRepository.java', '''
package com.lawfirm.app.repository;

import com.lawfirm.app.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);
}
''')
write('repository/ClientRepository.java', '''
package com.lawfirm.app.repository;

import com.lawfirm.app.entity.Client;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ClientRepository extends JpaRepository<Client, Long> {}
''')
write('repository/LawyerRepository.java', '''
package com.lawfirm.app.repository;

import com.lawfirm.app.entity.Lawyer;
import org.springframework.data.jpa.repository.JpaRepository;

public interface LawyerRepository extends JpaRepository<Lawyer, Long> {}
''')
write('repository/LegalCaseRepository.java', '''
package com.lawfirm.app.repository;

import com.lawfirm.app.entity.CaseStatus;
import com.lawfirm.app.entity.LegalCase;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface LegalCaseRepository extends JpaRepository<LegalCase, Long> {
    List<LegalCase> findByStatus(CaseStatus status);
}
''')
write('repository/AppointmentRepository.java', '''
package com.lawfirm.app.repository;

import com.lawfirm.app.entity.Appointment;
import org.springframework.data.jpa.repository.JpaRepository;

public interface AppointmentRepository extends JpaRepository<Appointment, Long> {}
''')
write('repository/DocumentRepository.java', '''
package com.lawfirm.app.repository;

import com.lawfirm.app.entity.DocumentRecord;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DocumentRepository extends JpaRepository<DocumentRecord, Long> {}
''')
write('repository/ActivityLogRepository.java', '''
package com.lawfirm.app.repository;

import com.lawfirm.app.entity.ActivityLog;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface ActivityLogRepository extends JpaRepository<ActivityLog, Long> {
    List<ActivityLog> findTop10ByOrderByCreatedAtDesc();
}
''')

# security
write('security/JwtService.java', '''
package com.lawfirm.app.security;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

import javax.crypto.SecretKey;
import java.nio.charset.StandardCharsets;
import java.util.Base64;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

@Service
public class JwtService {
    @Value("${app.jwt.secret}")
    private String secret;

    @Value("${app.jwt.expiration-ms}")
    private long expirationMs;

    public String generateToken(String email, String role, Long userId) {
        Map<String, Object> claims = new HashMap<>();
        claims.put("role", role);
        claims.put("userId", userId);
        return Jwts.builder()
            .claims(claims)
            .subject(email)
            .issuedAt(new Date())
            .expiration(new Date(System.currentTimeMillis() + expirationMs))
            .signWith(getSigningKey(), Jwts.SIG.HS256)
            .compact();
    }

    public String extractEmail(String token) {
        return extractAllClaims(token).getSubject();
    }

    public boolean isTokenValid(String token, String email) {
        return extractEmail(token).equals(email) && !isTokenExpired(token);
    }

    public boolean isTokenExpired(String token) {
        return extractAllClaims(token).getExpiration().before(new Date());
    }

    private Claims extractAllClaims(String token) {
        return Jwts.parser()
            .verifyWith(getSigningKey())
            .build()
            .parseSignedClaims(token)
            .getPayload();
    }

    private SecretKey getSigningKey() {
        byte[] keyBytes = Base64.getDecoder().decode(Base64.getEncoder().encodeToString(secret.getBytes(StandardCharsets.UTF_8)));
        return Keys.hmacShaKeyFor(keyBytes);
    }
}
''')
write('security/UserDetailsServiceImpl.java', '''
package com.lawfirm.app.security;

import com.lawfirm.app.entity.User;
import com.lawfirm.app.repository.UserRepository;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class UserDetailsServiceImpl implements UserDetailsService {
    private final UserRepository userRepository;

    public UserDetailsServiceImpl(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserDetails loadUserByUsername(String email) throws UsernameNotFoundException {
        User user = userRepository.findByEmail(email)
            .orElseThrow(() -> new UsernameNotFoundException("User not found: " + email));

        return new org.springframework.security.core.userdetails.User(
            user.getEmail(),
            user.getPassword(),
            List.of(new SimpleGrantedAuthority("ROLE_" + user.getRole().name()))
        );
    }
}
''')
write('security/JwtAuthenticationFilter.java', '''
package com.lawfirm.app.security;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;

@Component
public class JwtAuthenticationFilter extends OncePerRequestFilter {
    private final JwtService jwtService;
    private final UserDetailsServiceImpl userDetailsService;

    public JwtAuthenticationFilter(JwtService jwtService, UserDetailsServiceImpl userDetailsService) {
        this.jwtService = jwtService;
        this.userDetailsService = userDetailsService;
    }

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain)
            throws ServletException, IOException {
        final String authHeader = request.getHeader("Authorization");
        if (authHeader == null || !authHeader.startsWith("Bearer ")) {
            filterChain.doFilter(request, response);
            return;
        }

        final String token = authHeader.substring(7);
        final String email = jwtService.extractEmail(token);

        if (email != null && SecurityContextHolder.getContext().getAuthentication() == null) {
            UserDetails userDetails = userDetailsService.loadUserByUsername(email);
            if (jwtService.isTokenValid(token, userDetails.getUsername())) {
                UsernamePasswordAuthenticationToken auth = new UsernamePasswordAuthenticationToken(
                    userDetails,
                    null,
                    userDetails.getAuthorities()
                );
                auth.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContextHolder.getContext().setAuthentication(auth);
            }
        }
        filterChain.doFilter(request, response);
    }
}
''')

# storage
write('storage/StorageService.java', '''
package com.lawfirm.app.storage;

import org.springframework.web.multipart.MultipartFile;
import java.nio.file.Path;

public interface StorageService {
    String store(MultipartFile file, String folderName);
    void deleteFile(String storedPath);
    Path resolve(String storedPath);
}
''')
write('storage/LocalStorageService.java', '''
package com.lawfirm.app.storage;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.UUID;

@Service
public class LocalStorageService implements StorageService {
    @Value("${app.storage.local.path}")
    private String localStoragePath;

    @Override
    public String store(MultipartFile file, String folderName) {
        try {
            Path root = Paths.get(localStoragePath, folderName).toAbsolutePath().normalize();
            Files.createDirectories(root);
            String safeName = UUID.randomUUID() + "-" + file.getOriginalFilename().replaceAll("[^a-zA-Z0-9._-]", "_");
            Path target = root.resolve(safeName);
            Files.copy(file.getInputStream(), target, StandardCopyOption.REPLACE_EXISTING);
            return target.toString();
        } catch (IOException e) {
            throw new IllegalStateException("Could not store file: " + e.getMessage(), e);
        }
    }

    @Override
    public void deleteFile(String storedPath) {
        try {
            if (storedPath != null && !storedPath.isBlank()) {
                Files.deleteIfExists(Paths.get(storedPath));
            }
        } catch (IOException e) {
            throw new IllegalStateException("Could not delete file: " + e.getMessage(), e);
        }
    }

    @Override
    public Path resolve(String storedPath) {
        return Paths.get(storedPath);
    }
}
''')

# DTOs
write('dto/AuthRequest.java', '''
package com.lawfirm.app.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

public class AuthRequest {
    @NotBlank
    @Email
    private String email;

    @NotBlank
    private String password;

    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPassword() { return password; }
    public void setPassword(String password) { this.password = password; }
}
''')
write('dto/AuthResponse.java', '''
package com.lawfirm.app.dto;

public class AuthResponse {
    private String token;
    private String email;
    private String role;
    private Long userId;

    public AuthResponse(String token, String email, String role, Long userId) {
        this.token = token;
        this.email = email;
        this.role = role;
        this.userId = userId;
    }

    public String getToken() { return token; }
    public void setToken(String token) { this.token = token; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getRole() { return role; }
    public void setRole(String role) { this.role = role; }
    public Long getUserId() { return userId; }
    public void setUserId(Long userId) { this.userId = userId; }
}
''')
write('dto/UserDto.java', '''
package com.lawfirm.app.dto;

public class UserDto {
    private Long id;
    private String firstName;
    private String lastName;
    private String email;
    private String phone;
    private String role;

    public UserDto() {}

    public UserDto(Long id, String firstName, String lastName, String email, String phone, String role) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.email = email;
        this.phone = phone;
        this.role = role;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFirstName() { return firstName; }
    public void setFirstName(String firstName) { this.firstName = firstName; }
    public String getLastName() { return lastName; }
    public void setLastName(String lastName) { this.lastName = lastName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getRole() { return role; }
    public void setRole(String role) { this.role = role; }
}
''')
write('dto/ClientDto.java', '''
package com.lawfirm.app.dto;

import java.time.LocalDate;

public class ClientDto {
    private Long id;
    private String fullName;
    private String email;
    private String phone;
    private String address;
    private LocalDate dateOfRegistration;
    private String clientType;
    private String notes;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
    public LocalDate getDateOfRegistration() { return dateOfRegistration; }
    public void setDateOfRegistration(LocalDate dateOfRegistration) { this.dateOfRegistration = dateOfRegistration; }
    public String getClientType() { return clientType; }
    public void setClientType(String clientType) { this.clientType = clientType; }
    public String getNotes() { return notes; }
    public void setNotes(String notes) { this.notes = notes; }
}
''')
write('dto/LawyerDto.java', '''
package com.lawfirm.app.dto;

public class LawyerDto {
    private Long id;
    private String fullName;
    private String email;
    private String phone;
    private String specialization;
    private int yearsOfExperience;
    private String barRegistrationNumber;
    private String availabilityStatus;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFullName() { return fullName; }
    public void setFullName(String fullName) { this.fullName = fullName; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getPhone() { return phone; }
    public void setPhone(String phone) { this.phone = phone; }
    public String getSpecialization() { return specialization; }
    public void setSpecialization(String specialization) { this.specialization = specialization; }
    public int getYearsOfExperience() { return yearsOfExperience; }
    public void setYearsOfExperience(int yearsOfExperience) { this.yearsOfExperience = yearsOfExperience; }
    public String getBarRegistrationNumber() { return barRegistrationNumber; }
    public void setBarRegistrationNumber(String barRegistrationNumber) { this.barRegistrationNumber = barRegistrationNumber; }
    public String getAvailabilityStatus() { return availabilityStatus; }
    public void setAvailabilityStatus(String availabilityStatus) { this.availabilityStatus = availabilityStatus; }
}
''')
write('dto/LegalCaseDto.java', '''
package com.lawfirm.app.dto;

import java.time.LocalDate;
import java.util.Set;

public class LegalCaseDto {
    private Long id;
    private String caseNumber;
    private String title;
    private String caseType;
    private Long clientId;
    private String clientName;
    private Set<Long> lawyerIds;
    private String courtName;
    private LocalDate filingDate;
    private LocalDate nextHearingDate;
    private String description;
    private String status;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getCaseNumber() { return caseNumber; }
    public void setCaseNumber(String caseNumber) { this.caseNumber = caseNumber; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public String getCaseType() { return caseType; }
    public void setCaseType(String caseType) { this.caseType = caseType; }
    public Long getClientId() { return clientId; }
    public void setClientId(Long clientId) { this.clientId = clientId; }
    public String getClientName() { return clientName; }
    public void setClientName(String clientName) { this.clientName = clientName; }
    public Set<Long> getLawyerIds() { return lawyerIds; }
    public void setLawyerIds(Set<Long> lawyerIds) { this.lawyerIds = lawyerIds; }
    public String getCourtName() { return courtName; }
    public void setCourtName(String courtName) { this.courtName = courtName; }
    public LocalDate getFilingDate() { return filingDate; }
    public void setFilingDate(LocalDate filingDate) { this.filingDate = filingDate; }
    public LocalDate getNextHearingDate() { return nextHearingDate; }
    public void setNextHearingDate(LocalDate nextHearingDate) { this.nextHearingDate = nextHearingDate; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
''')
write('dto/AppointmentDto.java', '''
package com.lawfirm.app.dto;

import java.time.LocalDate;
import java.time.LocalTime;

public class AppointmentDto {
    private Long id;
    private Long clientId;
    private String clientName;
    private Long lawyerId;
    private String lawyerName;
    private Long caseId;
    private LocalDate date;
    private LocalTime time;
    private String location;
    private String appointmentType;
    private String description;
    private String status;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Long getClientId() { return clientId; }
    public void setClientId(Long clientId) { this.clientId = clientId; }
    public String getClientName() { return clientName; }
    public void setClientName(String clientName) { this.clientName = clientName; }
    public Long getLawyerId() { return lawyerId; }
    public void setLawyerId(Long lawyerId) { this.lawyerId = lawyerId; }
    public String getLawyerName() { return lawyerName; }
    public void setLawyerName(String lawyerName) { this.lawyerName = lawyerName; }
    public Long getCaseId() { return caseId; }
    public void setCaseId(Long caseId) { this.caseId = caseId; }
    public LocalDate getDate() { return date; }
    public void setDate(LocalDate date) { this.date = date; }
    public LocalTime getTime() { return time; }
    public void setTime(LocalTime time) { this.time = time; }
    public String getLocation() { return location; }
    public void setLocation(String location) { this.location = location; }
    public String getAppointmentType() { return appointmentType; }
    public void setAppointmentType(String appointmentType) { this.appointmentType = appointmentType; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
''')
write('dto/DocumentDto.java', '''
package com.lawfirm.app.dto;

import java.time.LocalDateTime;

public class DocumentDto {
    private Long id;
    private String fileName;
    private String originalName;
    private String mimeType;
    private long fileSize;
    private LocalDateTime uploadedAt;
    private String uploadedBy;
    private Long caseId;
    private Long clientId;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getFileName() { return fileName; }
    public void setFileName(String fileName) { this.fileName = fileName; }
    public String getOriginalName() { return originalName; }
    public void setOriginalName(String originalName) { this.originalName = originalName; }
    public String getMimeType() { return mimeType; }
    public void setMimeType(String mimeType) { this.mimeType = mimeType; }
    public long getFileSize() { return fileSize; }
    public void setFileSize(long fileSize) { this.fileSize = fileSize; }
    public LocalDateTime getUploadedAt() { return uploadedAt; }
    public void setUploadedAt(LocalDateTime uploadedAt) { this.uploadedAt = uploadedAt; }
    public String getUploadedBy() { return uploadedBy; }
    public void setUploadedBy(String uploadedBy) { this.uploadedBy = uploadedBy; }
    public Long getCaseId() { return caseId; }
    public void setCaseId(Long caseId) { this.caseId = caseId; }
    public Long getClientId() { return clientId; }
    public void setClientId(Long clientId) { this.clientId = clientId; }
}
''')
write('dto/ActivityLogDto.java', '''
package com.lawfirm.app.dto;

import java.time.LocalDateTime;

public class ActivityLogDto {
    private Long id;
    private String actor;
    private String action;
    private String details;
    private LocalDateTime createdAt;

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getActor() { return actor; }
    public void setActor(String actor) { this.actor = actor; }
    public String getAction() { return action; }
    public void setAction(String action) { this.action = action; }
    public String getDetails() { return details; }
    public void setDetails(String details) { this.details = details; }
    public LocalDateTime getCreatedAt() { return createdAt; }
    public void setCreatedAt(LocalDateTime createdAt) { this.createdAt = createdAt; }
}
''')
write('dto/MonthlyCaseDto.java', '''
package com.lawfirm.app.dto;

public class MonthlyCaseDto {
    private String month;
    private long count;

    public String getMonth() { return month; }
    public void setMonth(String month) { this.month = month; }
    public long getCount() { return count; }
    public void setCount(long count) { this.count = count; }
}
''')
write('dto/DashboardDto.java', '''
package com.lawfirm.app.dto;

import java.util.List;
import java.util.Map;

public class DashboardDto {
    private long totalClients;
    private long totalLawyers;
    private long totalActiveCases;
    private long totalClosedCases;
    private long upcomingHearings;
    private long todaysAppointments;
    private List<LegalCaseDto> recentCases;
    private List<ActivityLogDto> recentActivities;
    private Map<String, Long> caseStatusDistribution;
    private List<MonthlyCaseDto> monthlyCaseRegistrations;

    public long getTotalClients() { return totalClients; }
    public void setTotalClients(long totalClients) { this.totalClients = totalClients; }
    public long getTotalLawyers() { return totalLawyers; }
    public void setTotalLawyers(long totalLawyers) { this.totalLawyers = totalLawyers; }
    public long getTotalActiveCases() { return totalActiveCases; }
    public void setTotalActiveCases(long totalActiveCases) { this.totalActiveCases = totalActiveCases; }
    public long getTotalClosedCases() { return totalClosedCases; }
    public void setTotalClosedCases(long totalClosedCases) { this.totalClosedCases = totalClosedCases; }
    public long getUpcomingHearings() { return upcomingHearings; }
    public void setUpcomingHearings(long upcomingHearings) { this.upcomingHearings = upcomingHearings; }
    public long getTodaysAppointments() { return todaysAppointments; }
    public void setTodaysAppointments(long todaysAppointments) { this.todaysAppointments = todaysAppointments; }
    public List<LegalCaseDto> getRecentCases() { return recentCases; }
    public void setRecentCases(List<LegalCaseDto> recentCases) { this.recentCases = recentCases; }
    public List<ActivityLogDto> getRecentActivities() { return recentActivities; }
    public void setRecentActivities(List<ActivityLogDto> recentActivities) { this.recentActivities = recentActivities; }
    public Map<String, Long> getCaseStatusDistribution() { return caseStatusDistribution; }
    public void setCaseStatusDistribution(Map<String, Long> caseStatusDistribution) { this.caseStatusDistribution = caseStatusDistribution; }
    public List<MonthlyCaseDto> getMonthlyCaseRegistrations() { return monthlyCaseRegistrations; }
    public void setMonthlyCaseRegistrations(List<MonthlyCaseDto> monthlyCaseRegistrations) { this.monthlyCaseRegistrations = monthlyCaseRegistrations; }
}
''')

# services
write('service/ActivityService.java', '''
package com.lawfirm.app.service;

import com.lawfirm.app.dto.ActivityLogDto;
import com.lawfirm.app.entity.ActivityLog;
import com.lawfirm.app.repository.ActivityLogRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ActivityService {
    private final ActivityLogRepository activityLogRepository;

    public ActivityService(ActivityLogRepository activityLogRepository) {
        this.activityLogRepository = activityLogRepository;
    }

    public void log(String actor, String action, String details) {
        activityLogRepository.save(new ActivityLog(actor, action, details));
    }

    public List<ActivityLogDto> getRecentActivities() {
        return activityLogRepository.findTop10ByOrderByCreatedAtDesc().stream().map(this::toDto).collect(Collectors.toList());
    }

    private ActivityLogDto toDto(ActivityLog activity) {
        ActivityLogDto dto = new ActivityLogDto();
        dto.setId(activity.getId());
        dto.setActor(activity.getActor());
        dto.setAction(activity.getAction());
        dto.setDetails(activity.getDetails());
        dto.setCreatedAt(activity.getCreatedAt());
        return dto;
    }
}
''')
write('service/UserService.java', '''
package com.lawfirm.app.service;

import com.lawfirm.app.dto.AuthRequest;
import com.lawfirm.app.dto.AuthResponse;
import com.lawfirm.app.dto.UserDto;
import com.lawfirm.app.entity.RoleName;
import com.lawfirm.app.entity.User;
import com.lawfirm.app.repository.UserRepository;
import com.lawfirm.app.security.JwtService;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class UserService {
    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final AuthenticationManager authenticationManager;
    private final JwtService jwtService;

    public UserService(UserRepository userRepository, PasswordEncoder passwordEncoder, AuthenticationManager authenticationManager, JwtService jwtService) {
        this.userRepository = userRepository;
        this.passwordEncoder = passwordEncoder;
        this.authenticationManager = authenticationManager;
        this.jwtService = jwtService;
    }

    public AuthResponse login(AuthRequest request) {
        authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(request.getEmail(), request.getPassword()));
        User user = userRepository.findByEmail(request.getEmail()).orElseThrow();
        String token = jwtService.generateToken(user.getEmail(), user.getRole().name(), user.getId());
        return new AuthResponse(token, user.getEmail(), user.getRole().name(), user.getId());
    }

    public UserDto register(String firstName, String lastName, String email, String password, String phone, RoleName role) {
        if (userRepository.findByEmail(email).isPresent()) {
            throw new IllegalArgumentException("User with email already exists");
        }
        User user = new User(firstName, lastName, email, passwordEncoder.encode(password), phone, role);
        User saved = userRepository.save(user);
        return toDto(saved);
    }

    public Optional<User> findByEmail(String email) {
        return userRepository.findByEmail(email);
    }

    private UserDto toDto(User user) {
        return new UserDto(user.getId(), user.getFirstName(), user.getLastName(), user.getEmail(), user.getPhone(), user.getRole().name());
    }
}
''')
write('service/ClientService.java', '''
package com.lawfirm.app.service;

import com.lawfirm.app.dto.ClientDto;
import com.lawfirm.app.entity.Client;
import com.lawfirm.app.repository.ClientRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ClientService {
    private final ClientRepository clientRepository;

    public ClientService(ClientRepository clientRepository) {
        this.clientRepository = clientRepository;
    }

    public List<ClientDto> findAll() {
        return clientRepository.findAll().stream().map(this::toDto).collect(Collectors.toList());
    }

    public ClientDto save(ClientDto dto) {
        Client client = dto.getId() != null ? clientRepository.findById(dto.getId()).orElse(new Client()) : new Client();
        client.setFullName(dto.getFullName());
        client.setEmail(dto.getEmail());
        client.setPhone(dto.getPhone());
        client.setAddress(dto.getAddress());
        client.setClientType(dto.getClientType());
        client.setNotes(dto.getNotes());
        if (dto.getDateOfRegistration() != null) client.setDateOfRegistration(dto.getDateOfRegistration());
        Client saved = clientRepository.save(client);
        return toDto(saved);
    }

    public ClientDto findById(Long id) {
        return toDto(clientRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("Client not found")));
    }

    public void delete(Long id) {
        clientRepository.deleteById(id);
    }

    private ClientDto toDto(Client client) {
        ClientDto dto = new ClientDto();
        dto.setId(client.getId());
        dto.setFullName(client.getFullName());
        dto.setEmail(client.getEmail());
        dto.setPhone(client.getPhone());
        dto.setAddress(client.getAddress());
        dto.setDateOfRegistration(client.getDateOfRegistration());
        dto.setClientType(client.getClientType());
        dto.setNotes(client.getNotes());
        return dto;
    }
}
''')
write('service/LawyerService.java', '''
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
''')
write('service/CaseService.java', '''
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
''')
write('service/AppointmentService.java', '''
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
''')
write('service/DocumentService.java', '''
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
''')
write('service/DashboardService.java', '''
package com.lawfirm.app.service;

import com.lawfirm.app.dto.ActivityLogDto;
import com.lawfirm.app.dto.DashboardDto;
import com.lawfirm.app.dto.LegalCaseDto;
import com.lawfirm.app.dto.MonthlyCaseDto;
import com.lawfirm.app.entity.ActivityLog;
import com.lawfirm.app.entity.CaseStatus;
import com.lawfirm.app.entity.LegalCase;
import com.lawfirm.app.repository.ActivityLogRepository;
import com.lawfirm.app.repository.AppointmentRepository;
import com.lawfirm.app.repository.ClientRepository;
import com.lawfirm.app.repository.LawyerRepository;
import com.lawfirm.app.repository.LegalCaseRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Service
public class DashboardService {
    private final ClientRepository clientRepository;
    private final LawyerRepository lawyerRepository;
    private final LegalCaseRepository legalCaseRepository;
    private final AppointmentRepository appointmentRepository;
    private final ActivityLogRepository activityLogRepository;

    public DashboardService(ClientRepository clientRepository, LawyerRepository lawyerRepository,
                           LegalCaseRepository legalCaseRepository, AppointmentRepository appointmentRepository,
                           ActivityLogRepository activityLogRepository) {
        this.clientRepository = clientRepository;
        this.lawyerRepository = lawyerRepository;
        this.legalCaseRepository = legalCaseRepository;
        this.appointmentRepository = appointmentRepository;
        this.activityLogRepository = activityLogRepository;
    }

    public DashboardDto buildDashboard() {
        DashboardDto dto = new DashboardDto();
        dto.setTotalClients(clientRepository.count());
        dto.setTotalLawyers(lawyerRepository.count());
        dto.setTotalActiveCases(legalCaseRepository.findByStatus(CaseStatus.ACTIVE).size());
        dto.setTotalClosedCases(legalCaseRepository.findByStatus(CaseStatus.CLOSED).size());
        dto.setUpcomingHearings(legalCaseRepository.findAll().stream().filter(c -> c.getNextHearingDate() != null && c.getNextHearingDate().isAfter(LocalDate.now())).count());
        dto.setTodaysAppointments(appointmentRepository.findAll().stream().filter(a -> a.getDate().equals(LocalDate.now())).count());

        List<LegalCase> recentCases = legalCaseRepository.findAll().stream()
            .sorted((a, b) -> b.getFilingDate().compareTo(a.getFilingDate()))
            .limit(5)
            .collect(Collectors.toList());
        dto.setRecentCases(recentCases.stream().map(this::toCaseDto).collect(Collectors.toList()));

        dto.setRecentActivities(activityLogRepository.findTop10ByOrderByCreatedAtDesc().stream().map(this::toActivityDto).collect(Collectors.toList()));

        Map<String, Long> distribution = new LinkedHashMap<>();
        for (CaseStatus status : CaseStatus.values()) {
            long count = legalCaseRepository.findAll().stream().filter(c -> c.getStatus() == status).count();
            distribution.put(status.name(), count);
        }
        dto.setCaseStatusDistribution(distribution);

        List<MonthlyCaseDto> monthly = new ArrayList<>();
        for (int i = 0; i < 6; i++) {
            LocalDate month = LocalDate.now().minusMonths(i);
            long count = legalCaseRepository.findAll().stream().filter(c -> c.getFilingDate() != null && c.getFilingDate().getMonthValue() == month.getMonthValue() && c.getFilingDate().getYear() == month.getYear()).count();
            MonthlyCaseDto item = new MonthlyCaseDto();
            item.setMonth(month.getMonth().name().substring(0, 3));
            item.setCount(count);
            monthly.add(0, item);
        }
        dto.setMonthlyCaseRegistrations(monthly);
        return dto;
    }

    private LegalCaseDto toCaseDto(LegalCase legalCase) {
        LegalCaseDto dto = new LegalCaseDto();
        dto.setId(legalCase.getId());
        dto.setCaseNumber(legalCase.getCaseNumber());
        dto.setTitle(legalCase.getTitle());
        dto.setCaseType(legalCase.getCaseType());
        dto.setClientName(legalCase.getClient() != null ? legalCase.getClient().getFullName() : null);
        dto.setStatus(legalCase.getStatus().name());
        return dto;
    }

    private ActivityLogDto toActivityDto(ActivityLog activity) {
        ActivityLogDto dto = new ActivityLogDto();
        dto.setId(activity.getId());
        dto.setActor(activity.getActor());
        dto.setAction(activity.getAction());
        dto.setDetails(activity.getDetails());
        dto.setCreatedAt(activity.getCreatedAt());
        return dto;
    }
}
''')

# controllers
write('controller/AuthController.java', '''
package com.lawfirm.app.controller;

import com.lawfirm.app.dto.AuthRequest;
import com.lawfirm.app.dto.AuthResponse;
import com.lawfirm.app.service.UserService;
import jakarta.validation.Valid;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/auth")
@CrossOrigin(origins = "*")
public class AuthController {
    private final UserService userService;

    public AuthController(UserService userService) {
        this.userService = userService;
    }

    @PostMapping("/login")
    public ResponseEntity<AuthResponse> login(@Valid @RequestBody AuthRequest request) {
        return ResponseEntity.ok(userService.login(request));
    }
}
''')
write('controller/DashboardController.java', '''
package com.lawfirm.app.controller;

import com.lawfirm.app.dto.DashboardDto;
import com.lawfirm.app.service.DashboardService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class DashboardController {
    private final DashboardService dashboardService;

    public DashboardController(DashboardService dashboardService) {
        this.dashboardService = dashboardService;
    }

    @GetMapping("/dashboard")
    public ResponseEntity<DashboardDto> getDashboard() {
        return ResponseEntity.ok(dashboardService.buildDashboard());
    }
}
''')
write('controller/ClientController.java', '''
package com.lawfirm.app.controller;

import com.lawfirm.app.dto.ClientDto;
import com.lawfirm.app.service.ClientService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/clients")
@CrossOrigin(origins = "*")
public class ClientController {
    private final ClientService clientService;

    public ClientController(ClientService clientService) {
        this.clientService = clientService;
    }

    @GetMapping
    public ResponseEntity<List<ClientDto>> all() {
        return ResponseEntity.ok(clientService.findAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<ClientDto> get(@PathVariable Long id) {
        return ResponseEntity.ok(clientService.findById(id));
    }

    @PostMapping
    public ResponseEntity<ClientDto> create(@RequestBody ClientDto dto) {
        return ResponseEntity.status(HttpStatus.CREATED).body(clientService.save(dto));
    }

    @PutMapping("/{id}")
    public ResponseEntity<ClientDto> update(@PathVariable Long id, @RequestBody ClientDto dto) {
        dto.setId(id);
        return ResponseEntity.ok(clientService.save(dto));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        clientService.delete(id);
        return ResponseEntity.noContent().build();
    }
}
''')
write('controller/LawyerController.java', '''
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
''')
write('controller/CaseController.java', '''
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
''')
write('controller/AppointmentController.java', '''
package com.lawfirm.app.controller;

import com.lawfirm.app.dto.AppointmentDto;
import com.lawfirm.app.service.AppointmentService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/appointments")
@CrossOrigin(origins = "*")
public class AppointmentController {
    private final AppointmentService appointmentService;

    public AppointmentController(AppointmentService appointmentService) {
        this.appointmentService = appointmentService;
    }

    @GetMapping
    public ResponseEntity<List<AppointmentDto>> all() {
        return ResponseEntity.ok(appointmentService.findAll());
    }

    @PostMapping
    public ResponseEntity<AppointmentDto> create(@RequestBody AppointmentDto dto) {
        return ResponseEntity.status(HttpStatus.CREATED).body(appointmentService.save(dto));
    }

    @PutMapping("/{id}")
    public ResponseEntity<AppointmentDto> update(@PathVariable Long id, @RequestBody AppointmentDto dto) {
        dto.setId(id);
        return ResponseEntity.ok(appointmentService.save(dto));
    }
}
''')
write('controller/DocumentController.java', '''
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
''')

# test
(backend / 'src' / 'test' / 'java' / 'com' / 'lawfirm' / 'app').mkdir(parents=True, exist_ok=True)
(backend / 'src' / 'test' / 'java' / 'com' / 'lawfirm' / 'app' / 'UserServiceTest.java').write_text(textwrap.dedent('''
    package com.lawfirm.app;

    import com.lawfirm.app.dto.AuthRequest;
    import com.lawfirm.app.entity.RoleName;
    import com.lawfirm.app.service.UserService;
    import org.junit.jupiter.api.Test;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.boot.test.context.SpringBootTest;

    import static org.junit.jupiter.api.Assertions.*;

    @SpringBootTest
    class UserServiceTest {

        @Autowired
        private UserService userService;

        @Test
        void registerUserShouldEncryptPassword() {
            var dto = userService.register("Test", "User", "user1@example.com", "Pass123!", "+1-000-0000", RoleName.STAFF);
            assertNotNull(dto);
            assertEquals("user1@example.com", dto.getEmail());
            assertNotEquals("Pass123!", userService.findByEmail("user1@example.com").orElseThrow().getPassword());
        }
    }
''').strip() + '\n', encoding='utf-8')

# general project docs
(root / 'README.md').write_text(textwrap.dedent('''
    # Cloud-Based Law Firm Management System

    This project implements a cloud-ready law firm management system with a Spring Boot backend and React frontend. It includes authentication, role-based access, client management, lawyer management, case tracking, appointments, document uploads, and dashboard analytics.

    ## Demo credentials
    - Email: admin@lawfirm.com
    - Password: Admin@123

    ## Run backend
    ```bash
    cd backend
    C:/Tools/apache-maven-3.9.9/bin/mvn.cmd spring-boot:run
    ```

    ## Run frontend
    ```bash
    cd frontend
    npm install
    npm run dev -- --host 0.0.0.0
    ```

    ## Docker Compose
    ```bash
    docker-compose up --build
    ```
''').strip() + '\n', encoding='utf-8')

(root / 'docker-compose.yml').write_text(textwrap.dedent('''
    version: '3.9'
    services:
      backend:
        build:
          context: ./backend
        ports:
          - "8080:8080"
        environment:
          SPRING_PROFILES_ACTIVE: docker
      frontend:
        build:
          context: ./frontend
        ports:
          - "5173:5173"
        depends_on:
          - backend
''').strip() + '\n', encoding='utf-8')

(backend / 'Dockerfile').write_text(textwrap.dedent('''
    FROM eclipse-temurin:17-jdk
    WORKDIR /app
    COPY . .
    RUN ./mvnw clean package -DskipTests || C:/Tools/apache-maven-3.9.9/bin/mvn.cmd clean package -DskipTests
    EXPOSE 8080
    CMD ["java", "-jar", "target/lawfirm-app-0.0.1-SNAPSHOT.jar"]
''').strip() + '\n', encoding='utf-8')

(frontend := root / 'frontend').mkdir(parents=True, exist_ok=True)
(frontend / 'package.json').write_text(textwrap.dedent('''
    {
      "name": "lawfirm-frontend",
      "private": true,
      "version": "1.0.0",
      "type": "module",
      "scripts": {
        "dev": "vite",
        "build": "tsc -b && vite build",
        "preview": "vite preview"
      },
      "dependencies": {
        "axios": "^1.7.9",
        "lucide-react": "^0.469.0",
        "react": "^19.0.0",
        "react-dom": "^19.0.0",
        "react-router-dom": "^7.0.0",
        "recharts": "^2.15.0"
      },
      "devDependencies": {
        "@types/react": "^19.0.0",
        "@types/react-dom": "^19.0.0",
        "@vitejs/plugin-react-swc": "^3.3.0",
        "autoprefixer": "^10.4.20",
        "postcss": "^8.4.49",
        "tailwindcss": "^3.4.16",
        "typescript": "^5.7.2",
        "vite": "^6.3.10"
      }
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'tsconfig.json').write_text(textwrap.dedent('''
    {
      "files": [],
      "references": [
        { "path": "./tsconfig.app.json" },
        { "path": "./tsconfig.node.json" }
      ]
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'tsconfig.app.json').write_text(textwrap.dedent('''
    {
      "compilerOptions": {
        "target": "ES2020",
        "useDefineForClassFields": true,
        "lib": ["ES2020", "DOM", "DOM.Iterable"],
        "allowJs": false,
        "skipLibCheck": true,
        "esModuleInterop": true,
        "allowSyntheticDefaultImports": true,
        "strict": true,
        "forceConsistentCasingInFileNames": true,
        "module": "ESNext",
        "moduleResolution": "Node",
        "resolveJsonModule": true,
        "isolatedModules": true,
        "noEmit": true,
        "jsx": "react-jsx"
      },
      "include": ["src"],
      "exclude": ["src/**/*.test.*"]
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'tsconfig.node.json').write_text(textwrap.dedent('''
    {
      "compilerOptions": {
        "composite": true,
        "skipLibCheck": true,
        "module": "ESNext",
        "moduleResolution": "Node",
        "allowSyntheticDefaultImports": true
      },
      "include": ["vite.config.ts"]
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'vite.config.ts').write_text(textwrap.dedent('''
    import { defineConfig } from 'vite'
    import react from '@vitejs/plugin-react-swc'

    export default defineConfig({
      plugins: [react()],
      server: {
        port: 5173,
        host: '0.0.0.0'
      }
    })
''').strip() + '\n', encoding='utf-8')
(frontend / 'tailwind.config.js').write_text(textwrap.dedent('''
    /** @type {import('tailwindcss').Config} */
    export default {
      content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
      theme: {
        extend: {}
      },
      plugins: []
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'postcss.config.js').write_text(textwrap.dedent('''
    export default {
      plugins: {
        tailwindcss: {},
        autoprefixer: {}
      }
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'index.html').write_text(textwrap.dedent('''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Law Firm Management</title>
      </head>
      <body class="bg-slate-100">
        <div id="root"></div>
        <script type="module" src="/src/main.tsx"></script>
      </body>
    </html>
''').strip() + '\n', encoding='utf-8')
(frontend / 'src').mkdir(parents=True, exist_ok=True)
(frontend / 'src' / 'main.tsx').write_text(textwrap.dedent('''
    import React from 'react'
    import ReactDOM from 'react-dom/client'
    import { BrowserRouter } from 'react-router-dom'
    import App from './App'
    import './index.css'

    ReactDOM.createRoot(document.getElementById('root')!).render(
      <React.StrictMode>
        <BrowserRouter>
          <App />
        </BrowserRouter>
      </React.StrictMode>
    )
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'types.ts').write_text(textwrap.dedent('''
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
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'api.ts').write_text(textwrap.dedent('''
    import axios from 'axios'

    const API_BASE_URL = 'http://localhost:8080/api'

    const api = axios.create({
      baseURL: API_BASE_URL
    })

    api.interceptors.request.use((config) => {
      const token = localStorage.getItem('token')
      if (token) {
        config.headers.Authorization = `Bearer ${token}`
      }
      return config
    })

    export const login = (email: string, password: string) => api.post('/auth/login', { email, password })
    export const getDashboard = () => api.get('/dashboard')
    export const getClients = () => api.get('/clients')
    export const createClient = (payload: any) => api.post('/clients', payload)
    export const updateClient = (id: number, payload: any) => api.put(`/clients/${id}`, payload)
    export const deleteClient = (id: number) => api.delete(`/clients/${id}`)
    export const getLawyers = () => api.get('/lawyers')
    export const createLawyer = (payload: any) => api.post('/lawyers', payload)
    export const updateLawyer = (id: number, payload: any) => api.put(`/lawyers/${id}`, payload)
    export const deleteLawyer = (id: number) => api.delete(`/lawyers/${id}`)
    export const getCases = () => api.get('/cases')
    export const createCase = (payload: any) => api.post('/cases', payload)
    export const updateCase = (id: number, payload: any) => api.put(`/cases/${id}`, payload)
    export const deleteCase = (id: number) => api.delete(`/cases/${id}`)
    export const getAppointments = () => api.get('/appointments')
    export const createAppointment = (payload: any) => api.post('/appointments', payload)
    export const updateAppointment = (id: number, payload: any) => api.put(`/appointments/${id}`, payload)
    export const getDocuments = () => api.get('/documents')
    export const uploadDocument = (form: FormData) => api.post('/documents', form, { headers: { 'Content-Type': 'multipart/form-data' } })
    export const deleteDocument = (id: number) => api.delete(`/documents/${id}`)

    export default api
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'App.tsx').write_text(textwrap.dedent('''
    import { Navigate, Route, Routes } from 'react-router-dom'
    import LoginPage from './pages/LoginPage'
    import DashboardPage from './pages/DashboardPage'
    import ClientsPage from './pages/ClientsPage'
    import LawyersPage from './pages/LawyersPage'
    import CasesPage from './pages/CasesPage'
    import AppointmentsPage from './pages/AppointmentsPage'
    import DocumentsPage from './pages/DocumentsPage'
    import Layout from './pages/Layout'

    const isAuthenticated = () => Boolean(localStorage.getItem('token'))

    export default function App() {
      return (
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route
            path="/"
            element={isAuthenticated() ? <Layout><DashboardPage /></Layout> : <Navigate to="/login" replace />}
          />
          <Route
            path="/clients"
            element={isAuthenticated() ? <Layout><ClientsPage /></Layout> : <Navigate to="/login" replace />}
          />
          <Route
            path="/lawyers"
            element={isAuthenticated() ? <Layout><LawyersPage /></Layout> : <Navigate to="/login" replace />}
          />
          <Route
            path="/cases"
            element={isAuthenticated() ? <Layout><CasesPage /></Layout> : <Navigate to="/login" replace />}
          />
          <Route
            path="/appointments"
            element={isAuthenticated() ? <Layout><AppointmentsPage /></Layout> : <Navigate to="/login" replace />}
          />
          <Route
            path="/documents"
            element={isAuthenticated() ? <Layout><DocumentsPage /></Layout> : <Navigate to="/login" replace />}
          />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      )
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'index.css').write_text(textwrap.dedent('''
    @tailwind base;
    @tailwind components;
    @tailwind utilities;

    body {
      margin: 0;
      font-family: Inter, sans-serif;
      background: #f8fafc;
      color: #0f172a;
    }

    * {
      box-sizing: border-box;
    }

    .card {
      @apply rounded-2xl border border-slate-200 bg-white p-4 shadow-sm;
    }
    .btn {
      @apply inline-flex items-center justify-center rounded-xl px-4 py-2 font-medium transition;
    }
    .btn-primary {
      @apply bg-blue-600 text-white hover:bg-blue-700;
    }
    .btn-secondary {
      @apply bg-slate-100 text-slate-700 hover:bg-slate-200;
    }
    .input {
      @apply w-full rounded-xl border border-slate-300 bg-white px-3 py-2 outline-none focus:border-blue-500;
    }
    .label {
      @apply mb-1 block text-sm font-medium text-slate-700;
    }
''').strip() + '\n', encoding='utf-8')

# pages
(frontend / 'src' / 'pages').mkdir(parents=True, exist_ok=True)
(frontend / 'src' / 'pages' / 'Layout.tsx').write_text(textwrap.dedent('''
    import { BarChart3, BriefcaseBusiness, CalendarDays, FolderOpen, Gavel, LogOut, Users } from 'lucide-react'
    import { Link, useLocation, useNavigate } from 'react-router-dom'

    const navItems = [
      { label: 'Dashboard', to: '/', icon: BarChart3 },
      { label: 'Clients', to: '/clients', icon: Users },
      { label: 'Lawyers', to: '/lawyers', icon: Gavel },
      { label: 'Cases', to: '/cases', icon: BriefcaseBusiness },
      { label: 'Appointments', to: '/appointments', icon: CalendarDays },
      { label: 'Documents', to: '/documents', icon: FolderOpen },
    ]

    export default function Layout({ children }: { children: React.ReactNode }) {
      const navigate = useNavigate()
      const location = useLocation()

      const handleLogout = () => {
        localStorage.removeItem('token')
        navigate('/login')
      }

      return (
        <div className="min-h-screen bg-slate-100">
          <div className="flex">
            <aside className="h-screen w-72 bg-slate-900 text-slate-100 p-5">
              <h1 className="mb-8 text-2xl font-bold">LegalFlow</h1>
              <nav className="space-y-2">
                {navItems.map(({ label, to, icon: Icon }) => (
                  <Link
                    key={to}
                    to={to}
                    className={`flex items-center gap-3 rounded-xl px-3 py-3 ${location.pathname === to ? 'bg-slate-700' : 'hover:bg-slate-800'}`}
                  >
                    <Icon size={18} />
                    {label}
                  </Link>
                ))}
              </nav>
              <button className="mt-8 flex w-full items-center gap-3 rounded-xl bg-slate-800 px-3 py-3 hover:bg-slate-700" onClick={handleLogout}>
                <LogOut size={18} />
                Logout
              </button>
            </aside>
            <main className="flex-1 p-6">{children}</main>
          </div>
        </div>
      )
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'pages' / 'LoginPage.tsx').write_text(textwrap.dedent('''
    import { useState } from 'react'
    import { useNavigate } from 'react-router-dom'
    import { login } from '../api'

    export default function LoginPage() {
      const [email, setEmail] = useState('admin@lawfirm.com')
      const [password, setPassword] = useState('Admin@123')
      const [error, setError] = useState('')
      const navigate = useNavigate()

      const submit = async (e: React.FormEvent) => {
        e.preventDefault()
        try {
          const response = await login(email, password)
          localStorage.setItem('token', response.data.token)
          navigate('/')
        } catch (err) {
          setError('Invalid credentials or backend not running')
        }
      }

      return (
        <div className="flex min-h-screen items-center justify-center bg-gradient-to-br from-slate-900 to-blue-800 p-6">
          <div className="w-full max-w-md rounded-2xl bg-white p-8 shadow-xl">
            <h1 className="mb-1 text-3xl font-bold">LegalFlow</h1>
            <p className="mb-6 text-slate-500">Cloud-based law firm management</p>
            <form className="space-y-4" onSubmit={submit}>
              <div>
                <label className="label">Email</label>
                <input className="input" value={email} onChange={(e) => setEmail(e.target.value)} />
              </div>
              <div>
                <label className="label">Password</label>
                <input type="password" className="input" value={password} onChange={(e) => setPassword(e.target.value)} />
              </div>
              {error && <p className="text-sm text-red-500">{error}</p>}
              <button className="btn btn-primary w-full" type="submit">Login</button>
            </form>
          </div>
        </div>
      )
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'pages' / 'DashboardPage.tsx').write_text(textwrap.dedent('''
    import { useEffect, useState } from 'react'
    import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts'
    import { getDashboard } from '../api'
    import type { DashboardData } from '../types'

    const COLORS = ['#2563eb', '#14b8a6', '#f59e0b', '#ef4444', '#8b5cf6', '#10b981']

    export default function DashboardPage() {
      const [data, setData] = useState<DashboardData | null>(null)

      useEffect(() => {
        getDashboard().then((res) => setData(res.data)).catch(() => setData(null))
      }, [])

      if (!data) return <div className="card">Loading dashboard…</div>

      const pieData = Object.entries(data.caseStatusDistribution || {}).map(([name, value]) => ({ name, value }))

      return (
        <div className="space-y-6">
          <div>
            <h2 className="text-3xl font-bold">Dashboard</h2>
            <p className="text-slate-500">Overview of legal operations</p>
          </div>

          <div className="grid md:grid-cols-2 xl:grid-cols-6 gap-4">
            {[
              ['Clients', data.totalClients],
              ['Lawyers', data.totalLawyers],
              ['Active Cases', data.totalActiveCases],
              ['Closed Cases', data.totalClosedCases],
              ['Upcoming Hearings', data.upcomingHearings],
              ['Today\'s Appointments', data.todaysAppointments],
            ].map(([label, value], index) => (
              <div key={label} className="card">
                <div className="text-sm text-slate-500">{label}</div>
                <div className="mt-2 text-3xl font-bold text-slate-800">{value}</div>
                <div className="mt-1 h-1 w-12 rounded bg-blue-500" style={{ opacity: 0.3 + index * 0.1 }} />
              </div>
            ))}
          </div>

          <div className="grid lg:grid-cols-2 gap-6">
            <div className="card">
              <h3 className="mb-4 text-lg font-semibold">Case Status Distribution</h3>
              <ResponsiveContainer width="100%" height={300}>
                <PieChart>
                  <Pie data={pieData} dataKey="value" nameKey="name" outerRadius={80} label>
                    {pieData.map((_, index) => (
                      <Cell key={index} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </div>
            <div className="card">
              <h3 className="mb-4 text-lg font-semibold">Monthly Case Registrations</h3>
              <ResponsiveContainer width="100%" height={300}>
                <BarChart data={data.monthlyCaseRegistrations || []}>
                  <XAxis dataKey="month" />
                  <YAxis />
                  <Tooltip />
                  <Bar dataKey="count" fill="#2563eb" radius={[8, 8, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </div>
          </div>

          <div className="grid lg:grid-cols-2 gap-6">
            <div className="card">
              <h3 className="mb-4 text-lg font-semibold">Recent Cases</h3>
              <div className="space-y-3">
                {(data.recentCases || []).slice(0, 5).map((c) => (
                  <div key={c.id} className="flex items-center justify-between border-b pb-2">
                    <div>
                      <div className="font-medium">{c.title}</div>
                      <div className="text-sm text-slate-500">{c.caseNumber}</div>
                    </div>
                    <span className="rounded-full bg-blue-100 px-2 py-1 text-xs text-blue-700">{c.status}</span>
                  </div>
                ))}
              </div>
            </div>
            <div className="card">
              <h3 className="mb-4 text-lg font-semibold">Recent Activities</h3>
              <div className="space-y-3">
                {(data.recentActivities || []).slice(0, 5).map((a) => (
                  <div key={a.id} className="border-b pb-2">
                    <div className="font-medium">{a.action}</div>
                    <div className="text-sm text-slate-500">{a.actor} · {new Date(a.createdAt).toLocaleString()}</div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      )
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'pages' / 'ClientsPage.tsx').write_text(textwrap.dedent('''
    import { useEffect, useState } from 'react'
    import { deleteClient, getClients, createClient, updateClient } from '../api'
    import type { Client } from '../types'

    const empty: Omit<Client, 'id'> = {
      fullName: '', email: '', phone: '', address: '', clientType: 'Individual', notes: ''
    }

    export default function ClientsPage() {
      const [clients, setClients] = useState<Client[]>([])
      const [form, setForm] = useState(empty)
      const [editingId, setEditingId] = useState<number | null>(null)

      const load = async () => {
        const res = await getClients()
        setClients(res.data)
      }

      useEffect(() => { load() }, [])

      const submit = async (e: React.FormEvent) => {
        e.preventDefault()
        if (editingId) await updateClient(editingId, form)
        else await createClient(form)
        setForm(empty)
        setEditingId(null)
        load()
      }

      const remove = async (id: number) => {
        await deleteClient(id)
        load()
      }

      return (
        <div className="space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-3xl font-bold">Clients</h2>
            <button className="btn btn-primary" onClick={() => setForm(empty)}>New Client</button>
          </div>
          <div className="grid lg:grid-cols-3 gap-6">
            <form className="card lg:col-span-1 space-y-3" onSubmit={submit}>
              <h3 className="text-xl font-semibold">{editingId ? 'Edit Client' : 'Add Client'}</h3>
              <input className="input" placeholder="Full name" value={form.fullName} onChange={(e) => setForm({ ...form, fullName: e.target.value })} />
              <input className="input" placeholder="Email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
              <input className="input" placeholder="Phone" value={form.phone} onChange={(e) => setForm({ ...form, phone: e.target.value })} />
              <input className="input" placeholder="Address" value={form.address} onChange={(e) => setForm({ ...form, address: e.target.value })} />
              <input className="input" placeholder="Client type" value={form.clientType} onChange={(e) => setForm({ ...form, clientType: e.target.value })} />
              <textarea className="input" placeholder="Notes" value={form.notes} onChange={(e) => setForm({ ...form, notes: e.target.value })} />
              <button className="btn btn-primary w-full" type="submit">Save</button>
            </form>

            <div className="card lg:col-span-2">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b text-slate-500">
                    <th className="py-2">Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                    <th>Type</th>
                    <th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {clients.map((client) => (
                    <tr key={client.id} className="border-b">
                      <td className="py-3">{client.fullName}</td>
                      <td>{client.email}</td>
                      <td>{client.phone}</td>
                      <td>{client.clientType}</td>
                      <td className="space-x-2 py-3">
                        <button className="btn btn-secondary" onClick={() => { setEditingId(client.id); setForm(client) }}>Edit</button>
                        <button className="btn btn-secondary" onClick={() => remove(client.id)}>Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'pages' / 'LawyersPage.tsx').write_text(textwrap.dedent('''
    import { useEffect, useState } from 'react'
    import { createLawyer, deleteLawyer, getLawyers, updateLawyer } from '../api'
    import type { Lawyer } from '../types'

    const empty: Omit<Lawyer, 'id'> = {
      fullName: '', email: '', phone: '', specialization: '', yearsOfExperience: 0, barRegistrationNumber: '', availabilityStatus: 'Available'
    }

    export default function LawyersPage() {
      const [lawyers, setLawyers] = useState<Lawyer[]>([])
      const [form, setForm] = useState(empty)
      const [editingId, setEditingId] = useState<number | null>(null)

      const load = async () => {
        const res = await getLawyers()
        setLawyers(res.data)
      }

      useEffect(() => { load() }, [])

      const submit = async (e: React.FormEvent) => {
        e.preventDefault()
        if (editingId) await updateLawyer(editingId, form)
        else await createLawyer(form)
        setForm(empty)
        setEditingId(null)
        load()
      }

      return (
        <div className="space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-3xl font-bold">Lawyers</h2>
            <button className="btn btn-primary" onClick={() => setForm(empty)}>New Lawyer</button>
          </div>
          <div className="grid lg:grid-cols-3 gap-6">
            <form className="card lg:col-span-1 space-y-3" onSubmit={submit}>
              <h3 className="text-xl font-semibold">{editingId ? 'Edit Lawyer' : 'Add Lawyer'}</h3>
              <input className="input" placeholder="Full name" value={form.fullName} onChange={(e) => setForm({ ...form, fullName: e.target.value })} />
              <input className="input" placeholder="Email" value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} />
              <input className="input" placeholder="Phone" value={form.phone} onChange={(e) => setForm({ ...form, phone: e.target.value })} />
              <input className="input" placeholder="Specialization" value={form.specialization} onChange={(e) => setForm({ ...form, specialization: e.target.value })} />
              <input className="input" type="number" placeholder="Experience years" value={form.yearsOfExperience} onChange={(e) => setForm({ ...form, yearsOfExperience: Number(e.target.value) })} />
              <input className="input" placeholder="Bar number" value={form.barRegistrationNumber} onChange={(e) => setForm({ ...form, barRegistrationNumber: e.target.value })} />
              <input className="input" placeholder="Availability" value={form.availabilityStatus} onChange={(e) => setForm({ ...form, availabilityStatus: e.target.value })} />
              <button className="btn btn-primary w-full">Save</button>
            </form>
            <div className="card lg:col-span-2">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b text-slate-500">
                    <th>Name</th><th>Specialization</th><th>Years</th><th>Status</th><th>Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {lawyers.map((lawyer) => (
                    <tr key={lawyer.id} className="border-b">
                      <td className="py-3">{lawyer.fullName}</td>
                      <td>{lawyer.specialization}</td>
                      <td>{lawyer.yearsOfExperience}</td>
                      <td>{lawyer.availabilityStatus}</td>
                      <td className="space-x-2 py-3">
                        <button className="btn btn-secondary" onClick={() => { setEditingId(lawyer.id); setForm(lawyer) }}>Edit</button>
                        <button className="btn btn-secondary" onClick={() => deleteLawyer(lawyer.id).then(load)}>Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'pages' / 'CasesPage.tsx').write_text(textwrap.dedent('''
    import { useEffect, useState } from 'react'
    import { createCase, deleteCase, getCases, updateCase } from '../api'
    import type { CaseItem } from '../types'

    const empty: Omit<CaseItem, 'id' | 'clientName'> = {
      caseNumber: '', title: '', caseType: '', clientId: 0, lawyerIds: [], courtName: '', filingDate: '', nextHearingDate: '', description: '', status: 'ACTIVE'
    }

    export default function CasesPage() {
      const [cases, setCases] = useState<CaseItem[]>([])
      const [form, setForm] = useState(empty)
      const [editingId, setEditingId] = useState<number | null>(null)

      const load = async () => {
        const res = await getCases()
        setCases(res.data)
      }

      useEffect(() => { load() }, [])

      const submit = async (e: React.FormEvent) => {
        e.preventDefault()
        if (editingId) await updateCase(editingId, form)
        else await createCase(form)
        setForm(empty)
        setEditingId(null)
        load()
      }

      return (
        <div className="space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-3xl font-bold">Cases</h2>
            <button className="btn btn-primary" onClick={() => setForm(empty)}>New Case</button>
          </div>
          <div className="grid lg:grid-cols-3 gap-6">
            <form className="card lg:col-span-1 space-y-3" onSubmit={submit}>
              <h3 className="text-xl font-semibold">{editingId ? 'Edit Case' : 'Add Case'}</h3>
              <input className="input" placeholder="Case number" value={form.caseNumber} onChange={(e) => setForm({ ...form, caseNumber: e.target.value })} />
              <input className="input" placeholder="Title" value={form.title} onChange={(e) => setForm({ ...form, title: e.target.value })} />
              <input className="input" placeholder="Case type" value={form.caseType} onChange={(e) => setForm({ ...form, caseType: e.target.value })} />
              <input className="input" type="number" placeholder="Client ID" value={form.clientId} onChange={(e) => setForm({ ...form, clientId: Number(e.target.value) })} />
              <input className="input" placeholder="Court name" value={form.courtName} onChange={(e) => setForm({ ...form, courtName: e.target.value })} />
              <input className="input" type="date" value={form.filingDate} onChange={(e) => setForm({ ...form, filingDate: e.target.value })} />
              <input className="input" type="date" value={form.nextHearingDate || ''} onChange={(e) => setForm({ ...form, nextHearingDate: e.target.value })} />
              <textarea className="input" placeholder="Description" value={form.description} onChange={(e) => setForm({ ...form, description: e.target.value })} />
              <input className="input" placeholder="Status" value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value })} />
              <button className="btn btn-primary w-full">Save</button>
            </form>
            <div className="card lg:col-span-2">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b text-slate-500"><th>Number</th><th>Title</th><th>Status</th><th>Actions</th></tr>
                </thead>
                <tbody>
                  {cases.map((c) => (
                    <tr key={c.id} className="border-b">
                      <td className="py-3">{c.caseNumber}</td>
                      <td>{c.title}</td>
                      <td>{c.status}</td>
                      <td className="space-x-2 py-3">
                        <button className="btn btn-secondary" onClick={() => { setEditingId(c.id); setForm(c) }}>Edit</button>
                        <button className="btn btn-secondary" onClick={() => deleteCase(c.id).then(load)}>Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'pages' / 'AppointmentsPage.tsx').write_text(textwrap.dedent('''
    import { useEffect, useState } from 'react'
    import { createAppointment, getAppointments, updateAppointment } from '../api'
    import type { Appointment } from '../types'

    const empty: Omit<Appointment, 'id' | 'clientName' | 'lawyerName'> = {
      clientId: 0, lawyerId: 0, caseId: 0, date: '', time: '', location: '', appointmentType: 'Hearing', description: '', status: 'SCHEDULED'
    }

    export default function AppointmentsPage() {
      const [items, setItems] = useState<Appointment[]>([])
      const [form, setForm] = useState(empty)

      const load = async () => {
        const res = await getAppointments()
        setItems(res.data)
      }

      useEffect(() => { load() }, [])

      const submit = async (e: React.FormEvent) => {
        e.preventDefault()
        await createAppointment(form)
        setForm(empty)
        load()
      }

      return (
        <div className="space-y-6">
          <h2 className="text-3xl font-bold">Appointments</h2>
          <div className="grid lg:grid-cols-3 gap-6">
            <form className="card lg:col-span-1 space-y-3" onSubmit={submit}>
              <input className="input" type="number" placeholder="Client ID" value={form.clientId} onChange={(e) => setForm({ ...form, clientId: Number(e.target.value) })} />
              <input className="input" type="number" placeholder="Lawyer ID" value={form.lawyerId} onChange={(e) => setForm({ ...form, lawyerId: Number(e.target.value) })} />
              <input className="input" type="number" placeholder="Case ID" value={form.caseId || 0} onChange={(e) => setForm({ ...form, caseId: Number(e.target.value) })} />
              <input className="input" type="date" value={form.date} onChange={(e) => setForm({ ...form, date: e.target.value })} />
              <input className="input" type="time" value={form.time} onChange={(e) => setForm({ ...form, time: e.target.value })} />
              <input className="input" placeholder="Location" value={form.location} onChange={(e) => setForm({ ...form, location: e.target.value })} />
              <input className="input" placeholder="Type" value={form.appointmentType} onChange={(e) => setForm({ ...form, appointmentType: e.target.value })} />
              <input className="input" placeholder="Description" value={form.description} onChange={(e) => setForm({ ...form, description: e.target.value })} />
              <input className="input" placeholder="Status" value={form.status} onChange={(e) => setForm({ ...form, status: e.target.value })} />
              <button className="btn btn-primary w-full" type="submit">Save Appointment</button>
            </form>
            <div className="card lg:col-span-2">
              <table className="w-full text-left">
                <thead>
                  <tr className="border-b text-slate-500"><th>Client</th><th>Lawyer</th><th>Date</th><th>Status</th></tr>
                </thead>
                <tbody>
                  {items.map((item) => (
                    <tr key={item.id} className="border-b">
                      <td className="py-3">{item.clientName}</td>
                      <td>{item.lawyerName}</td>
                      <td>{item.date}</td>
                      <td>{item.status}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )
    }
''').strip() + '\n', encoding='utf-8')
(frontend / 'src' / 'pages' / 'DocumentsPage.tsx').write_text(textwrap.dedent('''
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
''').strip() + '\n', encoding='utf-8')

print('Project scaffolding created successfully.')
