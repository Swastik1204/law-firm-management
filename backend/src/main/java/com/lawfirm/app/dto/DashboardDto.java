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
