package com.lawfirm.app.storage;

import org.springframework.web.multipart.MultipartFile;
import java.nio.file.Path;

public interface StorageService {
    String store(MultipartFile file, String folderName);
    void deleteFile(String storedPath);
    Path resolve(String storedPath);
}
