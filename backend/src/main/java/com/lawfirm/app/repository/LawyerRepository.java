package com.lawfirm.app.repository;

import com.lawfirm.app.entity.Lawyer;
import org.springframework.data.jpa.repository.JpaRepository;

public interface LawyerRepository extends JpaRepository<Lawyer, Long> {}
