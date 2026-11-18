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
