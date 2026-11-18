package com.lawfirm.app.service;

import com.lawfirm.app.dto.ClientDto;
import com.lawfirm.app.entity.Client;
import com.lawfirm.app.repository.ClientRepository;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ClientService {
    private final ClientRepository clientRepository;

    public ClientService(ClientRepository clientRepository) {
        this.clientRepository = clientRepository;
    }

    public List<ClientDto> findAll() {
        return clientRepository.findAll().stream().map(this::toDto).collect(Collectors.toList());
    }

    public ClientDto save(ClientDto dto) {
        Client client = dto.getId() != null ? clientRepository.findById(dto.getId()).orElse(new Client()) : new Client();
        client.setFullName(dto.getFullName());
        client.setEmail(dto.getEmail());
        client.setPhone(dto.getPhone());
        client.setAddress(dto.getAddress());
        client.setClientType(dto.getClientType());
        client.setNotes(dto.getNotes());
        if (dto.getDateOfRegistration() != null) client.setDateOfRegistration(dto.getDateOfRegistration());
        Client saved = clientRepository.save(client);
        return toDto(saved);
    }

    public ClientDto findById(Long id) {
        return toDto(clientRepository.findById(id).orElseThrow(() -> new IllegalArgumentException("Client not found")));
    }

    public void delete(Long id) {
        clientRepository.deleteById(id);
    }

    private ClientDto toDto(Client client) {
        ClientDto dto = new ClientDto();
        dto.setId(client.getId());
        dto.setFullName(client.getFullName());
        dto.setEmail(client.getEmail());
        dto.setPhone(client.getPhone());
        dto.setAddress(client.getAddress());
        dto.setDateOfRegistration(client.getDateOfRegistration());
        dto.setClientType(client.getClientType());
        dto.setNotes(client.getNotes());
        return dto;
    }
}
