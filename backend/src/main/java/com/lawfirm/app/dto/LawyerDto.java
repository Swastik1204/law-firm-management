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
