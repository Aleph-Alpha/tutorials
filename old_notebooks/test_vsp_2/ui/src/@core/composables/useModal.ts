import { ref } from 'vue'

export const useModal = () => {
  const shouldBeHidden = ref(false)
  const showModal = ref(false)

  function onCloseModal() {
    showModal.value = false
  }

  function onOpenModal() {
    showModal.value = true
  }

  function callActionOrOpenModal(actionCallback: () => void) {
    if (shouldBeHidden.value) {
      actionCallback()
    } else {
      onOpenModal()
    }
  }

  function getConfirmActionCallback(actionCallback: () => void) {
    return (checkboxChecked: boolean) => {
      actionCallback()
      shouldBeHidden.value = checkboxChecked
      onCloseModal()
    }
  }

  return {
    shouldBeHidden,
    showModal,
    onCloseModal,
    onOpenModal,
    callActionOrOpenModal,
    getConfirmActionCallback,
  }
}
