package com.lawfirm.app.repository;

import com.lawfirm.app.entity.DocumentRecord;
import org.springframework.data.jpa.repository.JpaRepository;

public interface DocumentRepository extends JpaRepository<DocumentRecord, Long> {}
