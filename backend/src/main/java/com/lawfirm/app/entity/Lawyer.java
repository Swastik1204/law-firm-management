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
