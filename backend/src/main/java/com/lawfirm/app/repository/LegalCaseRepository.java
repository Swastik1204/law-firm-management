package com.lawfirm.app.repository;

import com.lawfirm.app.entity.CaseStatus;
import com.lawfirm.app.entity.LegalCase;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.List;

public interface LegalCaseRepository extends JpaRepository<LegalCase, Long> {
    List<LegalCase> findByStatus(CaseStatus status);
}
