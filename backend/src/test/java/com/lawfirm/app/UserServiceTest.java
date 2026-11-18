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
