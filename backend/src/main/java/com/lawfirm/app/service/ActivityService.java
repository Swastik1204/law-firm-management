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
