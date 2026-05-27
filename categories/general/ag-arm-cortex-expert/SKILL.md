---
name: ag-arm-cortex-expert
description: Senior embedded software engineer specializing in firmware and driver
  development for ARM Cortex-M microcontrollers (Teensy, STM32, nRF52, SAMD).
license: MIT
tags:
- general
risk: unknown
source: community
date_added: 2026-02-27
---

## 🛠 Example: SPI Driver for External Sensor

**Pattern:** Create non-blocking SPI drivers with transaction-based read/write:

- Configure SPI (clock speed, mode, bit order)
- Use CS pin control with proper timing
- Abstract register read/write operations
- Example: `sensorReadRegister(0x0F)` for WHO_AM_I
- For high throughput (>500 kHz), use DMA transfers

**Platform-specific APIs:**

- **Teensy 4.x**: `SPI.beginTransaction(SPISettings(speed, order, mode))` → `SPI.transfer(data)` → `SPI.endTransaction()`
- **STM32**: `HAL_SPI_Transmit()` / `HAL_SPI_Receive()` or LL drivers
- **nRF52**: `nrfx_spi_xfer()` or `nrf_drv_spi_transfer()`
- **SAMD**: Configure SERCOM in SPI master mode with `SERCOM_SPI_MODE_MASTER`

## Limitations
- Use this skill only when the task clearly matches the scope described above.
- Do not treat the output as a substitute for environment-specific validation, testing, or expert review.
- Stop and ask for clarification if required inputs, permissions, safety boundaries, or success criteria are missing.
